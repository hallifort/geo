"""
GEO (Generative Engine Optimization) Audit Tool
READ-ONLY, ADDITIVE: produces "add this" recommendations only.
Never outputs "change this" instructions.
"""

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

        # Also save raw audit JSON for debugging
        json_path = OUTPUTS_DIR / f"{slug(url)}.json"
        json_path.write_text(json.dumps(audit, indent=2), encoding="utf-8")

    print("\nDone.")


if __name__ == "__main__":
    main()
