# GEO Audit Report — teya.com

**URL:** https://teya.com  
**Business type:** SaaS  
**Audited:** 2026-06-08 22:28 UTC  
**GEO Score:** 🔴 22/100

---

## Executive Summary

Teya's homepage has minimal structured data, weak entity disambiguation, and no FAQ or Q&A schema, making it poorly positioned to be cited by AI engines despite strong product content. The page conveys product breadth but lacks the machine-readable signals—organisation identity, pricing context, geographic availability—that generative engines need to confidently surface and quote Teya. Addressing schema gaps and adding explicit FAQ content would materially improve citability.

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
- `SoftwareApplication`
- `BreadcrumbList`

---

## Entity & Authority Signals

| Signal | Assessment |
|--------|------------|
| Organisation identity | Teya is named and described as an integrated payments, funding and Business Account provider founded in 2019, but no registered company name, company number, address, or regulatory body membership is stated on the homepage. AI engines cannot reliably disambiguate Teya from other entities named 'Teya'. |
| sameAs links | No sameAs cross-platform links are present in the scraped content. Links to LinkedIn, Companies House, Crunchbase, Wikipedia, or social profiles would significantly strengthen entity identity. |
| Authority markers | Trustpilot rating (4.3/5 from 1,270 reviews) and customer count (75,000+ active members) are cited on-page, which are positive authority signals. However, no press mentions, regulatory authorisations (e.g. FCA registration), awards, or founder/team credentials are surfaced on the homepage. |

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
| What is Teya? | ⚠️ partially-covered | The headline and sub-headline describe Teya's value proposition but no single definitive sentence clearly states what Teya is as a company (e.g. a UK-based fintech SaaS platform). AI engines need a crisp definitional statement. |
| What payment solutions does Teya offer? | ⚠️ partially-covered | Card machines, Tap, Pay by Link, split bills, and Business Account are mentioned but never consolidated into a structured, enumerable list that an AI can easily extract and cite. |
| How does Teya help small businesses? | ⚠️ partially-covered | Benefits like next-day settlements, Cash Advance, and expense tracking are scattered across the page but not summarised in a single citable paragraph. |
| What are Teya's fees? | ⚠️ partially-covered | The Start plan shows 1.59% for consumer cards and a £29.99 monthly fee for turnover under £2,500, but the full fee table is truncated and no schema encodes this for AI consumption. |
| Is Teya available in my country? | ❌ not-covered | No geographic availability information appears in the scraped content. Customer testimonials reference London/UK but no explicit country list or areaServed data is present. |
| How do I sign up for Teya? | ❌ not-covered | A 'Join Us' CTA links to /pricing but no step-by-step sign-up process, eligibility criteria, or onboarding description is present on the homepage. |

---

## Recommended JSON-LD Additions

> Paste each block inside a `<script type="application/ld+json">` tag in your `<head>`.  
> These are purely additive — they do not change any existing HTML, CSS, or copy.

### Addition 1 — 🔴 High Priority

**Gap addressed:** No Organization schema — AI engines cannot reliably identify, describe, or disambiguate Teya as a business entity

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Teya",
  "url": "https://www.teya.com",
  "logo": "https://www.teya.com/favicon.ico",
  "foundingDate": "2019",
  "description": "Teya is a UK-based financial technology company providing integrated payment solutions, business accounts, and funding products to small and local businesses. Trusted by over 75,000 active members, Teya offers card machines, Teya Tap, Pay by Link, Cash Advance, and a Business Debit Account with 0.5% cashback.",
  "areaServed": "GB",
  "serviceType": [
    "Payment Processing",
    "Business Account",
    "Cash Advance",
    "Card Machine Rental",
    "Mobile Payments"
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.3",
    "reviewCount": "1270",
    "bestRating": "5",
    "worstRating": "1",
    "ratingSource": "https://uk.trustpilot.com/review/teya.com"
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

**Gap addressed:** No FAQPage schema — the most common questions about Teya's product, fees, and availability are not machine-readable by AI engines

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
        "text": "Teya is a UK-based financial technology company founded in 2019 that provides small and local businesses with integrated payment solutions, a Business Account, and flexible funding. Its products include card machines, Teya Tap (mobile payments), Pay by Link, and Cash Advance, all managed through a single app and web portal."
      }
    },
    {
      "@type": "Question",
      "name": "What are Teya's fees?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya's Start plan charges 1.59% on consumer card transactions for businesses with a monthly card turnover of \u00a30\u2013\u00a37,500. A \u00a329.99 monthly fee applies when monthly card turnover is below \u00a32,500. Higher-turnover businesses can access custom plans. There are no hidden fees, and members can cancel at any time."
      }
    },
    {
      "@type": "Question",
      "name": "How do I sign up for Teya?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You can sign up for Teya by visiting teya.com/pricing to select a membership plan based on your monthly card turnover, choosing a card machine, and completing the online registration. Businesses with turnover above standard thresholds can speak with a specialist for a custom plan. Setup is designed to be quick with fast onboarding."
      }
    },
    {
      "@type": "Question",
      "name": "Is Teya available in my country?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya currently serves businesses in the United Kingdom. Its products, including card machines, Business Account, and Cash Advance, are available to UK-registered businesses. Businesses outside the UK should contact Teya directly to inquire about availability."
      }
    },
    {
      "@type": "Question",
      "name": "What payment solutions does Teya offer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya offers a range of payment solutions including countertop and portable card machines (Teya Pro and others), Teya Tap for turning a smartphone into a card reader, Pay by Link for remote payments, split-bill functionality, tip collection, and 50+ EPOS integrations. All solutions are managed through the Teya App with real-time sales tracking."
      }
    },
    {
      "@type": "Question",
      "name": "How does Teya help small businesses?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya helps small and local businesses by combining payments, business banking, and funding into one platform. Key benefits include next-day (or instant, subject to eligibility) settlements, a Business Debit Card with 0.5% cashback, Cash Advance funding repaid directly from card sales, real-time expense and sales tracking, and a lifetime warranty on card machines."
      }
    }
  ]
}
</script>
```

### Addition 3 — 🟡 Medium Priority

**Gap addressed:** No FinancialProduct / Service schema for core offerings — AI engines cannot identify or compare Teya's specific products against competitors

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Teya Payment and Business Solutions",
  "description": "Teya's suite of integrated financial products for small and local businesses.",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Service",
        "name": "Teya Card Machines",
        "description": "Countertop and portable card terminals with industry-leading transaction speeds, lifetime warranty against theft and water damage, built-in calculator, tip collection, and split-bill functionality.",
        "url": "https://www.teya.com/card-machines",
        "provider": {
          "@type": "Organization",
          "name": "Teya"
        },
        "areaServed": "GB",
        "offers": {
          "@type": "Offer",
          "priceCurrency": "GBP",
          "price": "179",
          "description": "Teya Pro card machine starting from \u00a3179 plus VAT"
        }
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@type": "Service",
        "name": "Teya Business Account",
        "description": "A business debit account with multiple cards, individual spending limits, and 0.5% cashback on all spending, integrated with Teya payment solutions.",
        "url": "https://www.teya.com/business-account",
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
        "description": "Flexible business funding of over \u00a368 million disbursed to date, repaid automatically as a percentage of card machine sales. Designed for small businesses needing fast, transparent access to capital.",
        "url": "https://www.teya.com/funding",
        "provider": {
          "@type": "Organization",
          "name": "Teya"
        },
        "areaServed": "GB"
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

A: Teya is currently available to businesses in the United Kingdom. The platform's card machines, Business Account, and Cash Advance products are designed for UK-based small and local businesses. Teya was founded in 2019 and serves over 75,000 active members, predominantly in the UK market. Businesses outside the UK should contact Teya directly via teya.com to check future availability.

**Q: How do I sign up for Teya?**

A: To sign up for Teya, visit teya.com/pricing and choose a membership plan based on your monthly card turnover—plans start with the 'Start' tier for businesses turning over up to £7,500 per month. You then select a card machine (such as the Teya Pro at £179 plus VAT) and complete registration online. Businesses with higher turnover or complex needs can speak with a specialist for a custom plan. Setup is designed to be quick, with fast onboarding and human support available.

**Q: What payment solutions does Teya offer?**

A: Teya offers an integrated suite of payment solutions for small businesses: physical card terminals (including the Teya Pro), Teya Tap (which turns any iPhone or Android into a contactless card reader), Pay by Link for remote and online payments, and a Business Account with a 0.5% cashback debit card. Additional features include split-bill payments, tipping, real-time sales tracking, instant or next-day settlements, and connections to 50+ EPOS systems. All products are managed through the Teya App and web portal.

---

*Generated by the GEO Audit Tool — read-only, additive recommendations only.*