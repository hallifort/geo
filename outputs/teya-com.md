# GEO Audit Report — teya.com

**URL:** https://teya.com  
**Business type:** SaaS  
**Audited:** 2026-06-08 22:50 UTC  
**GEO Score:** 🔴 22/100

---

## Executive Summary

Teya's homepage communicates its value proposition clearly in human-readable copy but is critically under-structured for AI engines: no JSON-LD schema is detectable, key entity signals (founding date, headquarters, regulatory status) are absent from the page, and none of the top questions an AI would answer about Teya are covered in a discrete, citable format. Adding Organisation, Product, and FAQPage schema—plus three targeted FAQ blocks—would meaningfully improve citation probability across ChatGPT, Perplexity, and Google AI Overviews.

---

## Schema.org Coverage

**Present:** None detected

**Missing / recommended:**
- `Organization`
- `FAQPage`
- `Product`
- `FinancialProduct`
- `WebSite`
- `SoftwareApplication`
- `AggregateRating`
- `Review`

---

## Entity & Authority Signals

| Signal | Assessment |
|--------|------------|
| Organisation identity | Weak. The page names 'Teya' and references founding in 2019, 75,000+ active members, and a UK customer-support base, but no registered company name, company number, regulator, or headquarters address is present on the scraped homepage. |
| sameAs links | Absent. No links to LinkedIn, Companies House, Crunchbase, Wikipedia, or other authoritative cross-platform identity sources are visible in the scraped content. |
| Authority markers | Partial. Trustpilot rating (4.3/5 from 1,270 reviews) and headline statistics (609 million+ transactions in 2025, £68 million+ in Cash Advance) are present but not encoded in machine-readable schema, so AI engines cannot reliably extract them. |

---

## Meta Signals

| Signal | Status |
|--------|--------|
| datePublished | absent |
| author | absent |
| canonical | unclear |

---

## Top-Question Coverage

| Question | Coverage | Note |
|----------|----------|------|
| What is Teya? | ⚠️ partially-covered | The hero headline and sub-copy describe Teya as an integrated payments, funding and Business Account provider for local businesses, but there is no concise, standalone definition an AI can cleanly extract and cite. |
| What payment solutions does Teya offer? | ⚠️ partially-covered | Card machines, Tap-to-pay, Pay by Link, split payments, and EPOS integrations are all mentioned, but they are scattered across UI components rather than presented as a structured, enumerable list. |
| How does Teya help small businesses? | ⚠️ partially-covered | Benefits like next-day settlements, Cash Advance, 0.5% cashback, real-time sales tracking, and lifetime warranty are present but not consolidated into a single citable passage. |
| What are Teya's fees? | ⚠️ partially-covered | The Start plan consumer card rate of 1.59% and a £29.99 monthly fee for sub-£2,500 turnover are mentioned, but higher tiers are truncated and no full fee schedule is presented in a citable block. |
| Is Teya available in my country? | ❌ not-covered | No geographic availability information appears anywhere in the scraped content; the only location signal is a reference to UK-based customer support. |
| How do I sign up for Teya? | ❌ not-covered | The page has 'Join Us' and 'Check our offers' CTAs linking to /pricing, but there is no description of the sign-up process, required documents, or onboarding steps. |

---

## Recommended JSON-LD Additions

> Paste each block inside a `<script type="application/ld+json">` tag in your `<head>`.  
> These are purely additive — they do not change any existing HTML, CSS, or copy.

### Addition 1 — 🔴 High Priority

**Gap addressed:** No Organization schema — AI engines cannot reliably identify Teya as a distinct entity with founding date, geography, ratings, or cross-platform links

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Teya",
  "url": "https://www.teya.com",
  "foundingDate": "2019",
  "description": "Teya is a fintech company founded in 2019 that provides integrated payment solutions, business accounts, and funding products to small and local businesses. Teya serves over 75,000 active members and has processed more than 609 million transactions in 2025.",
  "areaServed": {
    "@type": "Country",
    "name": "United Kingdom"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer support",
    "areaServed": "GB",
    "availableLanguage": "English"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.3",
    "bestRating": "5",
    "worstRating": "1",
    "reviewCount": "1270",
    "ratingCount": "1270"
  },
  "sameAs": [
    "https://uk.trustpilot.com/review/teya.com"
  ]
}
</script>
```

### Addition 2 — 🔴 High Priority

**Gap addressed:** No FAQPage schema — the six key questions users and AI engines ask about Teya are unanswered in a machine-readable format, severely limiting citation potential

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is Teya?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya is a fintech company founded in 2019 that offers an integrated suite of payment, business account, and funding solutions designed specifically for small and local businesses. It serves over 75,000 active members and enables businesses to accept card payments in-person and remotely, manage cash flow, and access growth funding."
      }
    },
    {
      "@type": "Question",
      "name": "What payment solutions does Teya offer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya offers a range of payment solutions including physical card terminals (Teya Pro and other card machines), Teya Tap (turning a smartphone into a card machine), Pay by Link for remote payments, split-bill functionality, and over 50 EPOS integrations. All solutions are supported by next-day and instant settlement options."
      }
    },
    {
      "@type": "Question",
      "name": "What are Teya's fees?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya uses a membership plan model based on monthly card turnover. The Start plan, for businesses processing up to \u00a37,500 per month, charges 1.59% on consumer card transactions. A \u00a329.99 monthly fee applies when card turnover is below \u00a32,500. Teya states there are no hidden fees, and custom plans are available for higher-volume businesses."
      }
    },
    {
      "@type": "Question",
      "name": "How does Teya help small businesses?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya helps small businesses by combining payments, a business debit account with 0.5% cashback, real-time sales tracking, and a Cash Advance funding product (with over \u00a368 million disbursed) into a single platform. Additional benefits include next-day settlements, a lifetime warranty on card machines, industry-leading transaction speeds, and UK-based human customer support."
      }
    },
    {
      "@type": "Question",
      "name": "How do I sign up for Teya?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You can sign up for Teya by visiting teya.com/pricing to select a membership plan that matches your monthly card turnover. Setup is described as quick, and businesses can cancel anytime. For higher-volume or custom requirements, Teya offers a specialist sales consultation."
      }
    },
    {
      "@type": "Question",
      "name": "Is Teya available in my country?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya currently serves businesses in the United Kingdom, with UK-based customer support. For information on availability in other countries, visit teya.com or contact the Teya sales team."
      }
    }
  ]
}
</script>
```

### Addition 3 — 🟡 Medium Priority

**Gap addressed:** No SoftwareApplication or FinancialProduct schema — Teya's core products (card machines, Business Account, Cash Advance) are invisible to AI product-comparison queries

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Teya Products",
  "description": "Teya's integrated suite of payment, account, and funding products for small businesses.",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "FinancialProduct",
        "name": "Teya Card Machines",
        "description": "Physical card terminals including the Teya Pro (\u00a3179 + VAT) that accept contactless, chip-and-PIN, and mobile payments in-person. Features include split bills, tipping, integrated calculator, instant settlement, and a lifetime warranty.",
        "url": "https://www.teya.com/card-machines",
        "provider": {
          "@type": "Organization",
          "name": "Teya"
        }
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@type": "FinancialProduct",
        "name": "Teya Business Account",
        "description": "A business debit account with multiple cards, individual spending limits, and 0.5% cashback on all spending, integrated with Teya's payment and sales management tools.",
        "url": "https://www.teya.com/business-account",
        "provider": {
          "@type": "Organization",
          "name": "Teya"
        }
      }
    },
    {
      "@type": "ListItem",
      "position": 3,
      "item": {
        "@type": "FinancialProduct",
        "name": "Teya Cash Advance",
        "description": "Flexible business funding repaid automatically as a percentage of daily card machine sales. Teya has provided over \u00a368 million in Cash Advance funding to small businesses.",
        "url": "https://www.teya.com/funding",
        "provider": {
          "@type": "Organization",
          "name": "Teya"
        }
      }
    }
  ]
}
</script>
```

---

## Citation-Ready FAQ Blocks

> Paste these as visible Q&A sections on your page (e.g. in a `<details>` accordion or a  
> dedicated FAQ section). They are purely additive.

**Q: Is Teya available in my country?**

A: Teya currently operates in the United Kingdom, where it serves over 75,000 small and local businesses with in-person and remote payment solutions, a business account, and cash advance funding. UK-based human customer support is available to all members. For the latest information on expansion to other countries, visit teya.com or contact the Teya sales team directly.

**Q: How do I sign up for Teya?**

A: To sign up for Teya, visit teya.com/pricing and choose a membership plan based on your monthly card turnover—plans start with the 'Start' tier for businesses processing up to £7,500 per month at a 1.59% consumer card rate. Teya describes the setup process as quick, with no long-term lock-in (cancel anytime). Businesses with higher turnover or complex needs can book a consultation with a Teya specialist for a custom plan.

**Q: What are Teya's fees?**

A: Teya charges transaction fees based on a tiered membership plan aligned to monthly card turnover. The entry-level 'Start' plan applies a 1.59% fee on consumer card transactions for businesses turning over up to £7,500 per month; a £29.99 monthly fee is added if turnover falls below £2,500. Teya emphasises simple, transparent rates with no hidden fees, and offers custom pricing for higher-volume merchants.

---

*Generated by the GEO Audit Tool — read-only, additive recommendations only.*