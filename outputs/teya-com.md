# GEO Audit Report — teya.com

**URL:** https://teya.com  
**Business type:** SaaS  
**Audited:** 2026-06-08 22:57 UTC  
**GEO Score:** 🔴 28/100

---

## Executive Summary

Teya's homepage has reasonable on-page content about its products and trust signals but is critically under-served by structured data, lacking any detectable JSON-LD or Schema.org markup. Key GEO signals such as organisation identity, pricing transparency, geographic availability, and FAQ schema are absent, making it difficult for AI engines to confidently cite or summarise Teya in response to high-intent queries. Adding targeted structured data and explicit FAQ content would meaningfully improve citation likelihood.

---

## Schema.org Coverage

**Present:** None detected

**Missing / recommended:**
- `Organization`
- `WebSite`
- `FAQPage`
- `Product`
- `Service`
- `FinancialProduct`
- `AggregateRating`
- `Review`
- `SiteLinksSearchBox`

---

## Entity & Authority Signals

| Signal | Assessment |
|--------|------------|
| Organisation identity | Teya is named throughout the page and described as an integrated payments, funding, and business account provider founded in 2019, but no formal legal entity name, registration number, or headquarters address is surfaced in the scraped content. |
| sameAs links | No sameAs cross-platform links (LinkedIn, Companies House, Crunchbase, Wikipedia, etc.) are detectable in the scraped content, weakening entity disambiguation for AI engines. |
| Authority markers | Trustpilot rating of 4.3/5 from 1,270 reviews and a customer base of 75,000+ active members are present, which are useful authority signals, but they are embedded in widget markup rather than machine-readable structured data. |

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
| What is Teya? | ⚠️ partially-covered | The headline and sub-copy describe Teya's purpose but there is no concise, quotable definition paragraph an AI engine can cleanly extract as a standalone answer. |
| What payment solutions does Teya offer? | ⚠️ partially-covered | Card machines, Tap to Pay, Pay by Link, and split bills are mentioned but not consolidated into a structured, citable list with product names and descriptions in one place. |
| How does Teya help small businesses? | ⚠️ partially-covered | Benefits like next-day settlements, Cash Advance, and the Business Account are scattered across sections rather than presented as a consolidated, quotable answer. |
| What are Teya's fees? | ⚠️ partially-covered | A 1.59% consumer card rate for the Start plan and a £29.99 monthly fee condition are mentioned but full fee schedules across plans are truncated and not in structured data. |
| Is Teya available in my country? | ❌ not-covered | No geographic availability information is present on the homepage; UK is implied by references to UK-based support and GBP pricing but never explicitly stated. |
| How do I sign up for Teya? | ❌ not-covered | There are CTAs to 'Join Us' and 'Check our offers' but no step-by-step sign-up process or eligibility criteria are described in a way an AI engine could summarise. |

---

## Recommended JSON-LD Additions

> Paste each block inside a `<script type="application/ld+json">` tag in your `<head>`.  
> These are purely additive — they do not change any existing HTML, CSS, or copy.

### Addition 1 — 🔴 High Priority

**Gap addressed:** No Organization schema — AI engines cannot reliably identify Teya as a named entity, establish its founding date, geographic market, or link it to external authority sources

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Teya",
  "url": "https://www.teya.com",
  "foundingDate": "2019",
  "description": "Teya is a financial technology company founded in 2019 that provides integrated payment solutions, business accounts, and funding products to small and local businesses. Teya serves over 75,000 active members and offers card machines, Tap to Pay, Pay by Link, Cash Advance, and a Business Account with 0.5% cashback.",
  "areaServed": {
    "@type": "Country",
    "name": "United Kingdom"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.3",
    "bestRating": "5",
    "ratingCount": "1270",
    "reviewCount": "1270"
  },
  "sameAs": [
    "https://uk.trustpilot.com/review/teya.com"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer support",
    "areaServed": "GB",
    "availableLanguage": "English"
  }
}
</script>
```

### Addition 2 — 🔴 High Priority

**Gap addressed:** No FAQPage schema — the page does not answer high-intent questions in a machine-readable format, preventing AI engines and Google AI Overviews from surfacing Teya as a direct answer source

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
        "text": "Teya is a financial technology company founded in 2019 that provides integrated payments, business accounts, and funding solutions to small and local businesses. Its products include card machines, a Tap to Pay app, Pay by Link, Cash Advance funding, and a Business Account with 0.5% cashback. Teya is trusted by over 75,000 active members and processes hundreds of millions of transactions."
      }
    },
    {
      "@type": "Question",
      "name": "Is Teya available in my country?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya currently serves businesses in the United Kingdom. Its pricing is quoted in GBP and its customer support team is UK-based. Businesses outside the UK should check teya.com for the latest information on geographic availability."
      }
    },
    {
      "@type": "Question",
      "name": "How do I sign up for Teya?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "To sign up for Teya, visit teya.com and select a membership plan based on your monthly card turnover. Plans start from the 'Start' tier for businesses turning over up to \u00a37,500 per month. You can choose a card machine, set up a Business Account, and get started quickly with no long-term lock-in \u2014 Teya allows cancellation at any time."
      }
    }
  ]
}
</script>
```

### Addition 3 — 🟡 Medium Priority

**Gap addressed:** No FinancialProduct or Service schema for key offerings — AI engines cannot enumerate or describe Teya's specific payment products, their features, or fee structures in a structured way

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Teya Payment Solutions",
  "description": "Teya offers a range of integrated payment and financial products for small businesses in the UK.",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Service",
        "name": "Teya Card Machines",
        "description": "Physical card terminals including the Teya Pro, enabling in-person contactless and chip-and-pin payments with industry-leading transaction speeds, split bill functionality, built-in calculator, tipping, and a lifetime warranty covering theft and water damage.",
        "provider": {
          "@type": "Organization",
          "name": "Teya"
        },
        "areaServed": "GB",
        "offers": {
          "@type": "Offer",
          "price": "179",
          "priceCurrency": "GBP",
          "priceSpecification": {
            "@type": "UnitPriceSpecification",
            "price": "1.59",
            "priceCurrency": "GBP",
            "unitText": "% per consumer card transaction (Start plan)"
          }
        }
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@type": "Service",
        "name": "Teya Business Account",
        "description": "A business debit account with 0.5% cashback on all spending, the ability to create multiple cards with individual limits, and seamless integration with Teya card machine sales and expense tracking.",
        "provider": {
          "@type": "Organization",
          "name": "Teya"
        },
        "areaServed": "GB"
      }
    },
    {
      "@type": "ListItem",
      "position": 3,
      "item": {
        "@type": "Service",
        "name": "Teya Cash Advance",
        "description": "Flexible business funding repaid automatically as a percentage of daily card machine sales. Teya has advanced over \u00a368,000,000 to small businesses. Repayments are proportional to revenue, so businesses pay less during slower periods.",
        "provider": {
          "@type": "Organization",
          "name": "Teya"
        },
        "areaServed": "GB",
        "url": "https://www.teya.com/funding"
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

A: Teya currently operates in the United Kingdom, with GBP-denominated pricing and a UK-based customer support team. The company was founded in 2019 and serves over 75,000 active business members. Businesses outside the UK should visit teya.com to check whether Teya has expanded to additional markets.

**Q: How do I sign up for Teya?**

A: Signing up for Teya starts by selecting a membership plan at teya.com based on your monthly card turnover — the Start plan covers businesses processing up to £7,500 per month at a 1.59% consumer card rate. You then choose a card machine (such as the Teya Pro at £179 plus VAT) and can optionally open a Business Account. Teya offers a quick setup process with no long-term contract, and you can cancel at any time.

**Q: What are Teya's fees?**

A: Teya uses a tiered membership pricing model based on monthly card turnover. The Start plan (for businesses processing £0–£7,500/month) charges 1.59% on consumer card transactions, with a £29.99 monthly fee applied when turnover falls below £2,500. The Business Account includes a debit card with 0.5% cashback at no additional transaction cost. Enterprise and custom plans are available for higher-volume businesses. Full pricing details are at teya.com/pricing.

---

*Generated by the GEO Audit Tool — read-only, additive recommendations only.*