# GEO Audit Tool

Audit any website for **Generative Engine Optimization (GEO)** — how likely it is to be cited by AI engines like ChatGPT, Perplexity, Gemini, and Google AI Overviews.

## What it does

1. Reads a list of client URLs from `inputs/clients.csv`
2. Scrapes each URL to clean Markdown via the [Firecrawl](https://firecrawl.dev) API
3. Sends the content to Claude with a structured GEO audit prompt
4. Writes one Markdown report per client into `outputs/`

Each report contains:
- A **GEO score** (0–100)
- **Schema.org gap analysis** — which structured data types are present vs. missing
- **Entity & authority signals** — organisation identity, `sameAs` links, expertise markers
- **Meta signal check** — `datePublished`, `author`, `canonical`
- **Question coverage** — how well the site answers the client's top questions
- **3 ready-to-paste JSON-LD blocks** — the highest-impact structured data additions
- **3 citation-ready FAQ answer-blocks** — Q&A the client can paste directly onto the page

## The rule: additive only

This tool is **read-only and additive**. It never suggests changing existing HTML, CSS, copy, or layout. Every recommendation is a new block to paste in — nothing to modify or delete.

## Quickstart (GitHub Actions — no terminal needed)

1. **Fork or clone** this repository on GitHub.
2. **Add secrets:** go to *Settings → Secrets and variables → Actions → New repository secret* and add:
   - `FIRECRAWL_API_KEY` — your Firecrawl API key (get one at firecrawl.dev)
   - `ANTHROPIC_API_KEY` — your Anthropic API key
3. **Edit `inputs/clients.csv`** to add your client URLs (see format below).
4. **Run the workflow:** go to *Actions → GEO Audit → Run workflow → Run workflow*.
5. **Get reports:** once the run completes, reports are committed back to the branch automatically and also available as a downloadable ZIP artifact on the run page.

## `inputs/clients.csv` format

```csv
url,business_type,top_questions
https://example.com,SaaS,"What does Example do? How much does Example cost? Is Example secure?"
https://shop.example.com,ecommerce,"What products does Example sell? Does Example ship internationally?"
```

`business_type` options: `SaaS`, `ecommerce`, `local_business`, `content_blog` (or any descriptor).  
`top_questions`: 3–6 questions separated by `?`.

## Project layout

```
inputs/clients.csv                  Client list
outputs/                            Generated reports (auto-created)
templates/                          Reference JSON-LD skeletons
audit.py                            Main script
requirements.txt                    Python dependencies
.github/workflows/run-audit.yml     GitHub Actions workflow
CLAUDE.md                           Developer/AI context
```

## Requirements

- Python 3.10+
- A [Firecrawl](https://firecrawl.dev) account and API key
- An [Anthropic](https://console.anthropic.com) API key
