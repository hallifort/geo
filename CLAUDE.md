# GEO Audit Tool — Claude Context

## What this project does

This tool audits a client's website for **Generative Engine Optimization (GEO)** — how well the site is positioned to be cited, quoted, or summarised by AI engines (ChatGPT, Perplexity, Gemini, Google AI Overviews).

It produces a Markdown report per client with:
- A GEO health score (0–100)
- Schema.org coverage analysis (present vs. missing types)
- Entity/authority signal assessment
- Meta signal check (datePublished, author, canonical)
- Coverage of the client's top questions
- **3 ready-to-paste JSON-LD blocks** (the highest-priority additions)
- **3 citation-ready FAQ answer-blocks** (verbatim Q&A to paste on the page)

## The cardinal rule: READ-ONLY, ADDITIVE

This tool **never** instructs a client to change existing CSS, HTML structure, copy, or layout.  
Every recommendation is purely additive — "paste this new block into your `<head>`" or "add this FAQ section".  
If you modify the audit prompt or post-processing logic, preserve this constraint absolutely.

## Project structure

```
inputs/clients.csv          — one row per client (url, business_type, top_questions)
outputs/                    — generated reports land here (.md + .json per client)
templates/                  — reference JSON-LD skeletons (SaaS, ecommerce, local_business, content_blog)
audit.py                    — main script
requirements.txt            — Python deps (anthropic, httpx)
.github/workflows/run-audit.yml — GitHub Actions workflow (manual trigger)
```

## How to run

### Via GitHub Actions (no local setup needed)
1. Add `FIRECRAWL_API_KEY` and `ANTHROPIC_API_KEY` as repository secrets (Settings → Secrets → Actions).
2. Go to Actions → "GEO Audit" → "Run workflow".
3. Reports are committed back to the branch and also available as a downloadable artifact.

### Locally (if you have terminal access)
```bash
pip install -r requirements.txt
export FIRECRAWL_API_KEY=fc-...
export ANTHROPIC_API_KEY=sk-ant-...
python audit.py
```

## Adding clients

Edit `inputs/clients.csv`. Each row:
- `url` — the homepage or key landing page to scrape
- `business_type` — one of: `SaaS`, `ecommerce`, `local_business`, `content_blog` (or any free-text descriptor)
- `top_questions` — 3–6 questions the business should be the authoritative answer for, separated by `?`

## Environment variables

| Variable | Source | Purpose |
|----------|--------|---------|
| `FIRECRAWL_API_KEY` | GitHub secret | Authenticate to Firecrawl REST API for scraping |
| `ANTHROPIC_API_KEY` | GitHub secret | Authenticate to Claude API for GEO analysis |

Never hardcode these values.

## API details

- **Scraping:** Firecrawl REST API (`POST https://api.firecrawl.dev/v1/scrape`), markdown format, main content only.
- **Analysis:** Claude via the `anthropic` Python SDK, model `claude-sonnet-4-6`, structured JSON output.
- Retries: 3 attempts with exponential back-off for Firecrawl calls.

## Modifying the audit logic

The GEO audit prompt lives in `audit.py` → `GEO_SYSTEM_PROMPT` and `build_user_prompt()`.  
The JSON output schema is documented inside `GEO_SYSTEM_PROMPT`.  
The Markdown renderer is `render_report()`.

When changing the prompt, always verify the model still returns valid JSON matching the schema — the parser does `json.loads()` with no fallback.
