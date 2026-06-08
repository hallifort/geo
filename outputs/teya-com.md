# GEO Audit Report — teya.com

**URL:** https://teya.com  
**Business type:** SaaS  
**Audited:** 2026-06-08 22:19 UTC  
**GEO Score:** 🔴 22/100

---

## Executive Summary

Teya's homepage conveys its core value proposition but lacks structured data entirely, making it nearly invisible to AI engines that rely on schema signals for entity resolution. Key questions around fees, geographic availability, and sign-up process are either partially or not covered in a machine-readable or clearly citable format. Adding Organisation, Product, and FAQ schema—plus explicit FAQ copy—would significantly improve Teya's chances of being cited in AI-generated responses.

---

## Schema.org Coverage

**Present:** None detected

**Missing / recommended:**
- `Organization`
- `FAQPage`
- `Product`
- `Service`
- `FinancialProduct`
- `AggregateRating`
- `Review`
- `WebSite`
- `BreadcrumbList`

---

## Entity & Authority Signals

| Signal | Assessment |
|--------|------------|
| Organisation identity | Teya is named and described as an integrated payments, funding, and business account provider founded in 2019, but no registered company name, company number, or headquarters address is present in the scraped content, weakening entity resolution for AI engines. |
| sameAs links | No sameAs cross-platform links (LinkedIn, Crunchbase, Companies House, Wikipedia, etc.) are detectable in the scraped content, making it difficult for AI engines to corroborate Teya's identity across the web. |
| Authority markers | Trustpilot rating of 4.3/5 from 1,270 reviews is present, along with social proof metrics (75,000+ active members, 609M+ transactions in 2025, £68M+ in Cash Advance). However, these are rendered in visual/JS components rather than structured data, limiting their citability. |

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
| What is Teya? | ⚠️ partially-covered | The headline and sub-headline describe Teya as an integrated payments, funding, and Business Account solution for local businesses, but there is no concise, standalone definitional paragraph an AI can cleanly extract and quote. |
| What payment solutions does Teya offer? | ⚠️ partially-covered | Products such as card machines, Tap to Pay, Pay by Link, Business Account, and Cash Advance are listed, but they are fragmented across carousels and feature tiles rather than a structured, scannable list. |
| How does Teya help small businesses? | ⚠️ partially-covered | Key benefits like next-day settlements, no hidden fees, human support, and cashback are mentioned, and customer testimonials support this, but there is no consolidated paragraph addressing the question directly. |
| What are Teya's fees? | ⚠️ partially-covered | A 1.59% rate for consumer cards on the Start plan and a £29.99 monthly fee condition are visible, but the full fee table is truncated and not structured in a way AI engines can reliably parse or cite. |
| Is Teya available in my country? | ❌ not-covered | No geographic availability information appears in the scraped content. Customer testimonials reference London/UK but no explicit country or region list is provided. |
| How do I sign up for Teya? | ❌ not-covered | CTAs such as 'Join Us' and 'Check our offers' are present but no step-by-step sign-up process, eligibility criteria, or onboarding description exists on the page. |

---

## Recommended JSON-LD Additions

> Paste each block inside a `<script type="application/ld+json">` tag in your `<head>`.  
> These are purely additive — they do not change any existing HTML, CSS, or copy.

### Addition 1 — 🔴 High Priority

**Gap addressed:** Organisation identity and entity disambiguation — critical for AI engines to resolve who Teya is, where they operate, and how to cross-reference them

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Teya",
  "url": "https://www.teya.com",
  "logo": "https://www.teya.com/favicon.ico",
  "foundingDate": "2019",
  "description": "Teya is a financial technology company founded in 2019 that provides integrated payment solutions, business accounts, and funding products to small and local businesses. Its suite includes card machines, Tap to Pay, Pay by Link, a Business Debit Account with 0.5% cashback, and a Cash Advance product.",
  "areaServed": {
    "@type": "Country",
    "name": "United Kingdom"
  },
  "numberOfEmployees": {
    "@type": "QuantitativeValue",
    "description": "Serves 75,000+ active business members"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.3",
    "bestRating": "5",
    "ratingCount": "1270",
    "reviewAspect": "Trustpilot"
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

**Gap addressed:** FAQPage schema to directly answer the top questions AI engines are asked about Teya — fees, availability, sign-up, and product scope

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
        "text": "Teya is a UK-based financial technology company founded in 2019 that offers integrated payment solutions, a Business Account, and flexible funding for small and local businesses. Its products include card machines, Tap to Pay, Pay by Link, and a Cash Advance facility, all managed through a single app and web portal."
      }
    },
    {
      "@type": "Question",
      "name": "What are Teya's fees?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya operates a membership-based pricing model tied to monthly card turnover. The Start plan covers turnovers of \u00a30\u2013\u00a37,500 and charges 1.59% on consumer card transactions. A \u00a329.99 monthly fee applies when card turnover is under \u00a32,500. Teya states there are no hidden fees, and custom plans are available for higher-turnover businesses."
      }
    },
    {
      "@type": "Question",
      "name": "Is Teya available in my country?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya currently serves businesses in the United Kingdom. Its customer support team is UK-based. Businesses outside the UK should contact Teya directly to enquire about availability in other regions."
      }
    },
    {
      "@type": "Question",
      "name": "How do I sign up for Teya?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "To sign up for Teya, visit teya.com/pricing to select a membership plan based on your monthly card turnover, then choose a card machine. Setup is described as quick, and settlements begin as soon as the next business day. You can also speak with a Teya specialist for a custom plan."
      }
    },
    {
      "@type": "Question",
      "name": "How does Teya help small businesses?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya helps small and local businesses by combining card payments, a business debit account with 0.5% cashback, real-time sales tracking, and access to a Cash Advance of up to \u00a368 million distributed to date. Key benefits include next-day settlements, no hidden fees, lifetime warranty on hardware, 50+ EPOS integrations, and UK-based human customer support."
      }
    },
    {
      "@type": "Question",
      "name": "What payment solutions does Teya offer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya offers a full suite of payment solutions including physical card terminals (Teya Pro), a Tap to Pay mobile app (Teya Tap) that turns a smartphone into a card machine, Pay by Link for remote payments, split bill functionality, tipping, and instant or next-day settlements. All solutions are managed through the Teya App and web portal."
      }
    }
  ]
}
</script>
```

### Addition 3 — 🟡 Medium Priority

**Gap addressed:** FinancialProduct / Service schema to help AI engines understand and cite Teya's specific financial products — especially Cash Advance and Business Account

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Teya Financial Products and Services",
  "description": "Core products offered by Teya to small and local businesses in the UK",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "FinancialProduct",
        "name": "Teya Cash Advance",
        "description": "A flexible, fast, and transparent business funding product repaid directly from card machine sales. Teya has provided over \u00a368 million in Cash Advances to small businesses.",
        "url": "https://www.teya.com/funding",
        "provider": {
          "@type": "Organization",
          "name": "Teya",
          "url": "https://www.teya.com"
        },
        "areaServed": "GB"
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@type": "FinancialProduct",
        "name": "Teya Business Account",
        "description": "A business debit account with 0.5% cashback on all spending, the ability to create multiple cards with individual limits, and seamless integration with Teya payment terminals.",
        "url": "https://www.teya.com/business-account",
        "provider": {
          "@type": "Organization",
          "name": "Teya",
          "url": "https://www.teya.com"
        },
        "areaServed": "GB"
      }
    },
    {
      "@type": "ListItem",
      "position": 3,
      "item": {
        "@type": "Service",
        "name": "Teya Card Machines",
        "description": "Physical and mobile card payment terminals for in-person payments, including the Teya Pro device and Teya Tap app. Features include contactless payments, split bills, tipping, and a lifetime warranty covering theft and water damage.",
        "url": "https://www.teya.com/card-machines",
        "provider": {
          "@type": "Organization",
          "name": "Teya",
          "url": "https://www.teya.com"
        },
        "areaServed": "GB",
        "offers": {
          "@type": "Offer",
          "price": "179",
          "priceCurrency": "GBP",
          "description": "Teya Pro card machine starting price, plus VAT"
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

A: Teya currently operates in the United Kingdom, where it serves over 75,000 small and local businesses. Its customer support team is UK-based. Businesses outside the UK should visit teya.com or contact Teya directly to enquire about availability in other markets.

**Q: How do I sign up for Teya?**

A: Signing up for Teya starts at teya.com/pricing, where you select a membership plan based on your monthly card turnover. You then choose a card machine — such as the Teya Pro (from £179 + VAT) — and complete a quick setup process. Settlements begin from the next business day, and UK-based support is available throughout onboarding. Businesses with higher turnover can speak with a specialist for a custom plan.

**Q: What are Teya's fees?**

A: Teya uses a transparent, membership-based pricing model. The Start plan applies to businesses with up to £7,500 in monthly card turnover and charges 1.59% on consumer card transactions. A £29.99 monthly fee applies if turnover falls below £2,500. Teya advertises no hidden fees, and custom pricing is available for higher-volume businesses via a dedicated sales team.

---

*Generated by the GEO Audit Tool — read-only, additive recommendations only.*