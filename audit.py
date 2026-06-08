"""
GEO (Generative Engine Optimization) Audit Tool
READ-ONLY, ADDITIVE: produces "add this" recommendations only.
Never outputs "change this" instructions.
"""

import base64
import csv
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import anthropic
import httpx

FIRECRAWL_API_KEY = os.environ["FIRECRAWL_API_KEY"]
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]

FIRECRAWL_SCRAPE_URL = "https://api.firecrawl.dev/v1/scrape"
INPUTS_FILE = Path("inputs/clients.csv")
OUTPUTS_DIR = Path("outputs")


# ---------------------------------------------------------------------------
# Firecrawl
# ---------------------------------------------------------------------------

def scrape_url(url: str) -> str:
    """Scrape a URL via Firecrawl REST API and return clean markdown."""
    headers = {
        "Authorization": f"Bearer {FIRECRAWL_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "url": url,
        "formats": ["markdown"],
        "onlyMainContent": True,
        "timeout": 30000,
    }

    for attempt in range(1, 4):
        try:
            response = httpx.post(
                FIRECRAWL_SCRAPE_URL,
                headers=headers,
                json=payload,
                timeout=60,
            )
            response.raise_for_status()
            data = response.json()
            if data.get("success") and data.get("data", {}).get("markdown"):
                return data["data"]["markdown"]
            raise ValueError(f"Unexpected Firecrawl response: {data}")
        except httpx.HTTPStatusError as e:
            print(f"  Firecrawl HTTP error (attempt {attempt}/3): {e.response.status_code}")
            if attempt < 3:
                time.sleep(2 ** attempt)
        except Exception as e:
            print(f"  Firecrawl error (attempt {attempt}/3): {e}")
            if attempt < 3:
                time.sleep(2 ** attempt)

    raise RuntimeError(f"Failed to scrape {url} after 3 attempts")


# ---------------------------------------------------------------------------
# GEO audit prompt
# ---------------------------------------------------------------------------

GEO_SYSTEM_PROMPT = """You are an expert in Generative Engine Optimization (GEO) — the practice of making web content
more likely to be cited, quoted, or summarised by AI engines such as ChatGPT, Perplexity, Gemini, and Google AI Overviews.

You are operating in READ-ONLY, ADDITIVE mode. You must NEVER suggest changing existing CSS, HTML structure, copy,
or layout. You only produce "add this" recommendations: new JSON-LD blocks and new FAQ answer-blocks the client
can paste verbatim into their page.

Your output must always be a valid JSON object matching this exact schema:
{
  "summary": "2-3 sentence plain-English executive summary of GEO health",
  "schema_present": ["list of schema.org @types detected in the scraped content"],
  "schema_missing": ["list of schema.org @types that would be valuable but are absent"],
  "entity_signals": {
    "org_identity": "assessment of how clearly the organisation/author is identified",
    "sameAs_links": "assessment of cross-platform identity links present or absent",
    "authority_markers": "assessment of expertise/authoritativeness signals"
  },
  "meta_signals": {
    "datePublished": "present | absent | unclear",
    "author": "present | absent | unclear",
    "canonical": "present | absent | unclear"
  },
  "question_coverage": [
    {
      "question": "the question text",
      "coverage": "well-covered | partially-covered | not-covered",
      "note": "brief reason"
    }
  ],
  "json_ld_additions": [
    {
      "gap": "what this addresses",
      "priority": "high | medium | low",
      "code": { ... valid JSON-LD object ... }
    }
  ],
  "faq_blocks": [
    {
      "question": "question text",
      "answer": "concise, citable answer (2-4 sentences, factual, no fluff)"
    }
  ],
  "overall_geo_score": 42
}

Rules:
- json_ld_additions: exactly 3 items, highest-priority gaps first
- faq_blocks: exactly 3 items, matching the 3 most un-covered top questions
- overall_geo_score: integer 0-100 (0 = terrible GEO hygiene, 100 = perfect)
- All JSON-LD @context must be "https://schema.org"
- JSON-LD must be valid and immediately pasteable into a <script type="application/ld+json"> tag
- Do not wrap your response in markdown fences — return raw JSON only
"""


def build_user_prompt(url: str, business_type: str, top_questions: str, content: str) -> str:
    domain = urlparse(url).netloc
    questions_list = [q.strip() for q in top_questions.split("?") if q.strip()]
    questions_formatted = "\n".join(f"- {q}?" for q in questions_list)

    # Truncate content to keep within token limits (~12k chars ≈ ~3k tokens)
    content_truncated = content[:12000] + ("\n\n[content truncated]" if len(content) > 12000 else "")

    return f"""Audit the following website for GEO (Generative Engine Optimisation).

URL: {url}
Domain: {domain}
Business type: {business_type}

Top questions this business should be cited for:
{questions_formatted}

--- SCRAPED CONTENT (markdown) ---
{content_truncated}
--- END SCRAPED CONTENT ---

Produce the JSON audit report per your instructions. For the json_ld_additions, tailor the JSON-LD
specifically to this business (use real values from the scraped content wherever possible).
For faq_blocks, write concise, factually-grounded answers based on what you see in the scraped content.
"""


# ---------------------------------------------------------------------------
# Claude API
# ---------------------------------------------------------------------------

def run_geo_audit(url: str, business_type: str, top_questions: str, content: str) -> dict:
    """Send scraped content to Claude and return parsed audit JSON."""
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=GEO_SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": build_user_prompt(url, business_type, top_questions, content),
            }
        ],
    )

    raw = message.content[0].text.strip()

    # Strip accidental markdown fences if the model added them
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)

    return json.loads(raw)


# ---------------------------------------------------------------------------
# Report renderer
# ---------------------------------------------------------------------------

def score_badge(score: int) -> str:
    if score >= 70:
        return f"🟢 {score}/100"
    if score >= 40:
        return f"🟡 {score}/100"
    return f"🔴 {score}/100"


def render_report(url: str, business_type: str, audit: dict) -> str:
    domain = urlparse(url).netloc
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    score = audit.get("overall_geo_score", 0)

    lines = [
        f"# GEO Audit Report — {domain}",
        f"",
        f"**URL:** {url}  ",
        f"**Business type:** {business_type}  ",
        f"**Audited:** {now}  ",
        f"**GEO Score:** {score_badge(score)}",
        f"",
        f"---",
        f"",
        f"## Executive Summary",
        f"",
        audit.get("summary", ""),
        f"",
        f"---",
        f"",
        f"## Schema.org Coverage",
        f"",
        f"**Present:** {', '.join(audit.get('schema_present', [])) or 'None detected'}",
        f"",
        f"**Missing / recommended:**",
    ]
    for s in audit.get("schema_missing", []):
        lines.append(f"- `{s}`")

    lines += [
        f"",
        f"---",
        f"",
        f"## Entity & Authority Signals",
        f"",
    ]
    es = audit.get("entity_signals", {})
    lines.append(f"| Signal | Assessment |")
    lines.append(f"|--------|------------|")
    lines.append(f"| Organisation identity | {es.get('org_identity', '—')} |")
    lines.append(f"| sameAs links | {es.get('sameAs_links', '—')} |")
    lines.append(f"| Authority markers | {es.get('authority_markers', '—')} |")

    lines += [
        f"",
        f"---",
        f"",
        f"## Meta Signals",
        f"",
    ]
    ms = audit.get("meta_signals", {})
    lines.append(f"| Signal | Status |")
    lines.append(f"|--------|--------|")
    lines.append(f"| datePublished | {ms.get('datePublished', '—')} |")
    lines.append(f"| author | {ms.get('author', '—')} |")
    lines.append(f"| canonical | {ms.get('canonical', '—')} |")

    lines += [
        f"",
        f"---",
        f"",
        f"## Top-Question Coverage",
        f"",
        f"| Question | Coverage | Note |",
        f"|----------|----------|------|",
    ]
    for qc in audit.get("question_coverage", []):
        coverage_icon = {"well-covered": "✅", "partially-covered": "⚠️", "not-covered": "❌"}.get(
            qc.get("coverage", ""), "?"
        )
        lines.append(
            f"| {qc.get('question', '')} | {coverage_icon} {qc.get('coverage', '')} | {qc.get('note', '')} |"
        )

    lines += [
        f"",
        f"---",
        f"",
        f"## Recommended JSON-LD Additions",
        f"",
        f"> Paste each block inside a `<script type=\"application/ld+json\">` tag in your `<head>`.  ",
        f"> These are purely additive — they do not change any existing HTML, CSS, or copy.",
        f"",
    ]
    for i, addition in enumerate(audit.get("json_ld_additions", []), 1):
        priority_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(addition.get("priority", ""), "")
        lines.append(f"### Addition {i} — {priority_icon} {addition.get('priority', '').title()} Priority")
        lines.append(f"")
        lines.append(f"**Gap addressed:** {addition.get('gap', '')}")
        lines.append(f"")
        lines.append(f"```html")
        lines.append(f'<script type="application/ld+json">')
        lines.append(json.dumps(addition.get("code", {}), indent=2))
        lines.append(f"</script>")
        lines.append(f"```")
        lines.append(f"")

    lines += [
        f"---",
        f"",
        f"## Citation-Ready FAQ Blocks",
        f"",
        f"> Paste these as visible Q&A sections on your page (e.g. in a `<details>` accordion or a  ",
        f"> dedicated FAQ section). They are purely additive.",
        f"",
    ]
    for faq in audit.get("faq_blocks", []):
        lines.append(f"**Q: {faq.get('question', '')}**")
        lines.append(f"")
        lines.append(f"A: {faq.get('answer', '')}")
        lines.append(f"")

    lines.append(f"---")
    lines.append(f"")
    lines.append(f"*Generated by the GEO Audit Tool — read-only, additive recommendations only.*")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# HTML report renderer
# ---------------------------------------------------------------------------

def score_class(score: int) -> str:
    if score >= 70:
        return "score-high"
    if score >= 40:
        return "score-mid"
    return "score-low"


GEO_LOGO_PNG = Path("99f4cc43-7fb4-402d-b52e-576b603eb3ec.png")


def _geo_logo_img(height: int = 96) -> str:
    if GEO_LOGO_PNG.exists():
        b64 = base64.b64encode(GEO_LOGO_PNG.read_bytes()).decode()
        src = f"data:image/png;base64,{b64}"
    else:
        src = ""
    return f'<img src="{src}" alt="GEO" style="height:{height}px;width:auto;display:block"/>'


def render_html_report(url: str, business_type: str, audit: dict) -> str:
    domain = urlparse(url).netloc
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    score = audit.get("overall_geo_score", 0)
    es = audit.get("entity_signals", {})
    ms = audit.get("meta_signals", {})

    coverage_icon = {"well-covered": "✅", "partially-covered": "⚠️", "not-covered": "❌"}
    priority_label = {"high": "🔴 High", "medium": "🟡 Medium", "low": "🟢 Low"}

    def tag(value: str) -> str:
        cls = "tag-navy" if value in ("present", "well-covered") else "tag"
        return f'<span class="tag {cls}">{value}</span>'

    json_ld_sections = ""
    for i, addition in enumerate(audit.get("json_ld_additions", []), 1):
        pri = addition.get("priority", "")
        code = json.dumps(addition.get("code", {}), indent=2)
        json_ld_sections += f"""
        <div class="card card-accent" style="margin-bottom:var(--space-6)">
          <div style="display:flex;align-items:center;gap:var(--space-3);margin-bottom:var(--space-4)">
            <span class="tag">{priority_label.get(pri, pri)}</span>
            <strong class="serif">Addition {i}</strong>
          </div>
          <p style="margin:0 0 var(--space-4)"><strong>Gap addressed:</strong> {addition.get("gap", "")}</p>
          <pre><code>&lt;script type="application/ld+json"&gt;\n{code}\n&lt;/script&gt;</code></pre>
        </div>"""

    faq_sections = ""
    for faq in audit.get("faq_blocks", []):
        faq_sections += f"""
        <div class="card" style="margin-bottom:var(--space-4)">
          <p style="margin:0 0 var(--space-2)"><strong class="serif" style="color:var(--color-navy)">Q: {faq.get("question", "")}</strong></p>
          <p style="margin:0">A: {faq.get("answer", "")}</p>
        </div>"""

    question_rows = ""
    for qc in audit.get("question_coverage", []):
        icon = coverage_icon.get(qc.get("coverage", ""), "?")
        question_rows += f"""
          <tr>
            <td>{qc.get("question", "")}</td>
            <td>{icon} {qc.get("coverage", "")}</td>
            <td>{qc.get("note", "")}</td>
          </tr>"""

    schema_missing = "".join(
        f'<span class="tag" style="margin:2px">{s}</span>' for s in audit.get("schema_missing", [])
    )
    schema_present = ", ".join(audit.get("schema_present", [])) or "None detected"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GEO Audit — {domain}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
  <style>
    :root {{
      --color-bg: #EDE8DC;
      --color-navy: #1A1B6E;
      --color-cobalt: #2D35C8;
      --color-black: #0D0D0D;
      --color-white: #FFFFFF;
      --color-cobalt-10: rgba(45,53,200,0.10);
      --color-cobalt-20: rgba(45,53,200,0.20);
      --color-navy-10: rgba(26,27,110,0.10);
      --font-serif: 'Playfair Display', Georgia, serif;
      --font-sans: system-ui, -apple-system, sans-serif;
      --text-xs: 0.75rem; --text-sm: 0.875rem; --text-base: 1rem;
      --text-lg: 1.125rem; --text-xl: 1.25rem; --text-2xl: 1.5rem;
      --text-3xl: 1.875rem; --text-4xl: 2.25rem; --text-5xl: 3rem;
      --leading-tight: 1.2; --leading-normal: 1.5; --leading-loose: 1.75;
      --weight-regular: 400; --weight-semibold: 600; --weight-bold: 700;
      --space-1: 0.25rem; --space-2: 0.5rem; --space-3: 0.75rem;
      --space-4: 1rem; --space-5: 1.25rem; --space-6: 1.5rem;
      --space-8: 2rem; --space-10: 2.5rem; --space-12: 3rem;
      --space-16: 4rem; --space-20: 5rem; --space-24: 6rem;
      --radius-sm: 4px; --radius-md: 8px; --radius-lg: 12px; --radius-full: 9999px;
      --shadow-sm: 0 1px 3px rgba(26,27,110,0.12);
      --shadow-md: 0 4px 12px rgba(26,27,110,0.14);
      --shadow-lg: 0 8px 28px rgba(26,27,110,0.18);
    }}
    *, *::before, *::after {{ box-sizing: border-box; }}
    body {{
      background-color: var(--color-bg);
      color: var(--color-black);
      font-family: var(--font-sans);
      font-size: var(--text-base);
      line-height: var(--leading-normal);
      -webkit-font-smoothing: antialiased;
      max-width: 860px;
      margin: 0 auto;
      padding: var(--space-12) var(--space-6);
    }}
    h1, h2, h3, h4, h5, h6 {{
      font-family: var(--font-serif);
      font-weight: var(--weight-bold);
      line-height: var(--leading-tight);
      color: var(--color-navy);
    }}
    h1 {{ font-size: var(--text-5xl); margin: 0 0 var(--space-2); }}
    h2 {{ font-size: var(--text-3xl); margin: 0 0 var(--space-4); }}
    a {{ color: var(--color-cobalt); }}
    a:hover {{ color: var(--color-navy); }}
    .display {{
      font-family: var(--font-serif);
      font-style: italic;
      font-weight: var(--weight-bold);
      color: var(--color-navy);
    }}
    .card {{
      background-color: var(--color-white);
      border-radius: var(--radius-lg);
      padding: var(--space-8);
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--color-navy-10);
    }}
    .card-accent {{ border-top: 4px solid var(--color-cobalt); }}
    .score-badge {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 64px; height: 64px;
      border-radius: var(--radius-full);
      background-color: var(--color-cobalt);
      color: var(--color-white);
      font-family: var(--font-serif);
      font-size: var(--text-2xl);
      font-weight: var(--weight-bold);
      flex-shrink: 0;
    }}
    .score-high {{ background-color: var(--color-cobalt); }}
    .score-mid  {{ background-color: var(--color-navy); }}
    .score-low  {{ background-color: var(--color-black); }}
    .tag {{
      display: inline-block;
      padding: var(--space-1) var(--space-3);
      border-radius: var(--radius-full);
      font-size: var(--text-xs);
      font-weight: var(--weight-semibold);
      letter-spacing: 0.05em;
      text-transform: uppercase;
      background-color: var(--color-cobalt-10);
      color: var(--color-cobalt);
    }}
    .tag-navy {{ background-color: var(--color-navy-10); color: var(--color-navy); }}
    pre, code {{ font-family: 'Fira Code', 'Fira Mono', monospace; font-size: var(--text-sm); }}
    pre {{
      background-color: var(--color-navy);
      color: var(--color-bg);
      border-radius: var(--radius-md);
      padding: var(--space-6);
      overflow-x: auto;
      line-height: var(--leading-loose);
      white-space: pre-wrap;
      word-break: break-word;
    }}
    code {{
      background-color: var(--color-cobalt-10);
      color: var(--color-navy);
      padding: 0.1em 0.35em;
      border-radius: var(--radius-sm);
    }}
    pre code {{ background: none; color: inherit; padding: 0; }}
    .text-muted {{ color: rgba(13,13,13,0.5); }}
    .serif {{ font-family: var(--font-serif); }}
    table {{ width: 100%; border-collapse: collapse; font-size: var(--text-sm); }}
    th, td {{ text-align: left; padding: var(--space-3) var(--space-4); border-bottom: 1px solid var(--color-navy-10); }}
    th {{ font-family: var(--font-serif); font-weight: var(--weight-semibold); color: var(--color-navy); }}
    section {{ margin-bottom: var(--space-12); }}
    p {{ margin: 0 0 var(--space-4); line-height: var(--leading-normal); }}
  </style>
</head>
<body>

  <header style="margin-bottom:var(--space-12);display:flex;align-items:flex-start;gap:var(--space-8)">
    <div style="flex-shrink:0">
      {_geo_logo_img(96)}
    </div>
    <div style="flex:1;padding-top:var(--space-2)">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:var(--space-4)">
        <p class="text-muted" style="margin:0;font-size:var(--text-sm)">{now}</p>
        <img
          src="https://www.google.com/s2/favicons?domain={domain}&sz=64"
          alt="{domain} logo"
          style="width:40px;height:40px;object-fit:contain;background:transparent"
          onerror="this.style.display='none'"
        />
      </div>
      <h1 style="margin:0 0 var(--space-2)">GEO Audit Report</h1>
      <p class="display" style="font-size:var(--text-2xl);margin:0 0 var(--space-6)">{domain}</p>
      <div style="display:flex;align-items:center;gap:var(--space-4);flex-wrap:wrap">
        <div class="score-badge {score_class(score)}">{score}</div>
        <div>
          <p style="margin:0;font-size:var(--text-sm)" class="text-muted">GEO Health Score</p>
          <p style="margin:0"><strong>{url}</strong></p>
          <p style="margin:0" class="text-muted">{business_type}</p>
        </div>
      </div>
    </div>
  </header>

  <section>
    <h2>Executive Summary</h2>
    <p>{audit.get("summary", "")}</p>
  </section>

  <section>
    <h2>Schema.org Coverage</h2>
    <p><strong>Present:</strong> {schema_present}</p>
    <p><strong>Missing / recommended:</strong></p>
    <div style="display:flex;flex-wrap:wrap;gap:var(--space-2)">{schema_missing}</div>
  </section>

  <section>
    <h2>Entity &amp; Authority Signals</h2>
    <table>
      <thead><tr><th>Signal</th><th>Assessment</th></tr></thead>
      <tbody>
        <tr><td>Organisation identity</td><td>{es.get("org_identity", "—")}</td></tr>
        <tr><td>sameAs links</td><td>{es.get("sameAs_links", "—")}</td></tr>
        <tr><td>Authority markers</td><td>{es.get("authority_markers", "—")}</td></tr>
      </tbody>
    </table>
  </section>

  <section>
    <h2>Meta Signals</h2>
    <table>
      <thead><tr><th>Signal</th><th>Status</th></tr></thead>
      <tbody>
        <tr><td>datePublished</td><td>{tag(ms.get("datePublished", "—"))}</td></tr>
        <tr><td>author</td><td>{tag(ms.get("author", "—"))}</td></tr>
        <tr><td>canonical</td><td>{tag(ms.get("canonical", "—"))}</td></tr>
      </tbody>
    </table>
  </section>

  <section>
    <h2>Top-Question Coverage</h2>
    <table>
      <thead><tr><th>Question</th><th>Coverage</th><th>Note</th></tr></thead>
      <tbody>{question_rows}</tbody>
    </table>
  </section>

  <section>
    <h2>Recommended JSON-LD Additions</h2>
    <p class="text-muted">Paste each block inside a <code>&lt;script type="application/ld+json"&gt;</code> tag in your <code>&lt;head&gt;</code>. Purely additive — no existing HTML or CSS changes required.</p>
    {json_ld_sections}
  </section>

  <section>
    <h2>Citation-Ready FAQ Blocks</h2>
    <p class="text-muted">Paste these as a visible Q&amp;A section on your page. Purely additive.</p>
    {faq_sections}
  </section>

  <footer style="margin-top:var(--space-16);padding-top:var(--space-6);border-top:1px solid var(--color-navy-10)">
    <p class="text-muted" style="font-size:var(--text-sm)">Generated by the GEO Audit Tool — read-only, additive recommendations only.</p>
  </footer>

</body>
</html>"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def slug(url: str) -> str:
    domain = urlparse(url).netloc.replace("www.", "")
    return re.sub(r"[^\w-]", "-", domain).strip("-")


def main():
    if not INPUTS_FILE.exists():
        print(f"ERROR: {INPUTS_FILE} not found.", file=sys.stderr)
        sys.exit(1)

    OUTPUTS_DIR.mkdir(exist_ok=True)

    with open(INPUTS_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        clients = list(reader)

    print(f"GEO Audit Tool — processing {len(clients)} client(s)\n")

    for i, client in enumerate(clients, 1):
        url = client["url"].strip()
        business_type = client["business_type"].strip()
        top_questions = client["top_questions"].strip()

        print(f"[{i}/{len(clients)}] {url}")
        print(f"  Scraping via Firecrawl...")

        try:
            content = scrape_url(url)
            print(f"  Scraped {len(content):,} chars of markdown")
        except RuntimeError as e:
            print(f"  SKIP: {e}")
            continue

        print(f"  Running GEO audit via Claude...")
        try:
            audit = run_geo_audit(url, business_type, top_questions, content)
        except (json.JSONDecodeError, anthropic.APIError) as e:
            print(f"  SKIP: audit failed — {e}")
            continue

        score = audit.get("overall_geo_score", "?")
        print(f"  GEO score: {score}/100")

        report_md = render_report(url, business_type, audit)
        out_path = OUTPUTS_DIR / f"{slug(url)}.md"
        out_path.write_text(report_md, encoding="utf-8")
        print(f"  Report written: {out_path}")

        html_path = OUTPUTS_DIR / f"{slug(url)}.html"
        html_path.write_text(render_html_report(url, business_type, audit), encoding="utf-8")
        print(f"  HTML report:    {html_path}")

        # Also save raw audit JSON for debugging
        json_path = OUTPUTS_DIR / f"{slug(url)}.json"
        json_path.write_text(json.dumps(audit, indent=2), encoding="utf-8")

    print("\nDone.")


if __name__ == "__main__":
    main()
