# GEO Audit Report — teya.com

**URL:** https://teya.com  
**Business type:** SaaS  
**Audited:** 2026-06-08 23:12 UTC  
**GEO Score:** 🔴 28/100

---

## Executive Summary

Teya's homepage has strong product messaging and social proof but is critically under-structured for AI citation: no JSON-LD schema is detectable, organisational identity signals are weak, and key questions around fees, geography, and sign-up are only partially answered in the scraped content. Adding Organisation, Product, and FAQ structured data would substantially improve Teya's likelihood of being cited by generative engines.

---

## Schema.org Coverage

**Present:** None detected

**Missing / recommended:**
- `Organization`
- `WebSite`
- `FAQPage`
- `Product`
- `FinancialProduct`
- `AggregateRating`
- `Review`
- `Service`
- `BreadcrumbList`

---

## Entity & Authority Signals

| Signal | Assessment |
|--------|------------|
| Organisation identity | Teya is named and described as an integrated payments, funding, and business account provider founded in 2019, but no registered company name, company number, headquarters address, or legal entity details are present on the page. |
| sameAs links | No sameAs cross-platform links (LinkedIn, Companies House, Crunchbase, Wikipedia, etc.) are detectable in the scraped content. |
| Authority markers | Some authority signals exist: 75,000+ active members, 4.3/5 Trustpilot rating from 1,270 reviews, £68M+ in Cash Advance issued, and 609M+ transactions processed in 2025. However, these are presented as raw text/UI elements rather than structured data, so AI engines cannot reliably extract them. |

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
| What is Teya? | ⚠️ partially-covered | The headline and subheadline describe Teya as an integrated payments, funding, and business account solution for local businesses, but there is no concise structured definition, founding context, or regulatory status that an AI engine can cleanly extract. |
| What payment solutions does Teya offer? | ⚠️ partially-covered | Card machines, Tap to Pay, Pay by Link, split bills, EPOS integrations, and instant settlements are mentioned, but they are spread across carousel/slider UI elements that are difficult for AI engines to parse as a structured list. |
| How does Teya help small businesses? | ✅ well-covered | Multiple angles are addressed: next-day settlements, cash advance funding, real-time sales tracking, cashback, lifetime warranty, and customer testimonials. This is the page's strongest coverage area. |
| What are Teya's fees? | ⚠️ partially-covered | The Start plan rate of 1.59% for consumer cards and a £29.99 monthly fee for sub-£2,500 turnover are mentioned, along with 0.5% cashback, but the full fee schedule is truncated and not structured for machine reading. |
| Is Teya available in my country? | ❌ not-covered | No countries or geographic markets are explicitly listed. Customer testimonials reference London/UK but no formal country availability list or supported markets section is present. |
| How do I sign up for Teya? | ❌ not-covered | CTAs like 'Join Us' and 'Check our offers' link to the pricing page, but there is no step-by-step sign-up process, onboarding description, or requirements outlined on the homepage. |

---

## Recommended JSON-LD Additions

> Paste each block inside a `<script type="application/ld+json">` tag in your `<head>`.  
> These are purely additive — they do not change any existing HTML, CSS, or copy.

### Addition 1 — 🔴 High Priority

**Gap addressed:** No Organisation entity — AI engines cannot identify who Teya is, where they operate, or verify cross-platform identity

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Teya",
  "url": "https://www.teya.com",
  "logo": "https://www.teya.com/favicon.ico",
  "foundingDate": "2019",
  "description": "Teya is a financial technology company founded in 2019 that provides integrated payment solutions, business accounts, and funding products to small and local businesses. Trusted by over 75,000 customers, Teya offers card machines, Tap to Pay, Pay by Link, Cash Advance, and a Business Account with 0.5% cashback.",
  "slogan": "Empowering local businesses to thrive",
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
    "ratingCount": "1270",
    "reviewCount": "1270"
  },
  "sameAs": [
    "https://uk.trustpilot.com/review/teya.com"
  ]
}
</script>
```

### Addition 2 — 🔴 High Priority

**Gap addressed:** No FAQPage schema — the top questions about fees, sign-up, and country availability are not answered in a machine-readable format AI engines can cite

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
        "text": "Teya is a financial technology company founded in 2019 that provides integrated payment solutions, business accounts, and funding products designed for small and local businesses. Its platform combines card machines, Tap to Pay, Pay by Link, real-time sales tracking, Cash Advance funding, and a Business Account with 0.5% cashback \u2014 all in a single ecosystem trusted by over 75,000 customers."
      }
    },
    {
      "@type": "Question",
      "name": "What are Teya's fees?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya offers membership plans based on monthly card turnover. The Start plan covers \u00a30\u2013\u00a37,500 monthly turnover and charges 1.59% on consumer card transactions. A \u00a329.99 monthly fee applies when turnover is under \u00a32,500. Teya promotes simple, transparent rates with no hidden fees. Custom plans are available for businesses with higher turnover. Full plan details are available at teya.com/pricing."
      }
    },
    {
      "@type": "Question",
      "name": "How do I sign up for Teya?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You can sign up for Teya by visiting teya.com/pricing to select a membership plan based on your monthly card turnover, then choosing a card machine (such as the Teya Pro at \u00a3179 + VAT). Teya is designed for quick setup, and businesses can get started without long-term lock-in \u2014 you can cancel anytime. For higher-turnover businesses, a specialist consultation is available."
      }
    },
    {
      "@type": "Question",
      "name": "Is Teya available in my country?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya currently serves small and local businesses in the United Kingdom. Customer support is based in the UK. For information about availability in other markets, visit teya.com or contact the Teya sales team."
      }
    }
  ]
}
</script>
```

### Addition 3 — 🟡 Medium Priority

**Gap addressed:** No FinancialProduct or Service schema — Teya's core payment and funding products are invisible to AI knowledge graphs

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Teya Products and Services",
  "description": "Teya's suite of integrated financial and payment products for small businesses.",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "FinancialProduct",
        "name": "Teya Card Machines",
        "description": "Physical card terminals including the Teya Pro (\u00a3179 + VAT) with lifetime warranty covering theft and water damage, industry-leading transaction speeds, built-in calculator, tipping, split-bill, and instant settlements.",
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
        "description": "A debit account for small businesses with 0.5% cashback on all spending, the ability to create multiple cards with individual spending limits, and money transfer to any bank account.",
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
        "@type": "LoanOrCredit",
        "name": "Teya Cash Advance",
        "description": "Flexible, fast, and transparent business funding for small businesses, repaid directly as a percentage of card machine sales. Over \u00a368,000,000 in Cash Advance has been issued to Teya customers.",
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

A: Teya currently operates in the United Kingdom, serving over 75,000 small and local businesses. Its customer support team is UK-based. Teya has not publicly listed additional country markets on its homepage; businesses outside the UK should check teya.com or contact sales for the latest geographic availability.

**Q: How do I sign up for Teya?**

A: Signing up for Teya starts at teya.com/pricing, where you select a membership plan based on your monthly card turnover. You then choose a card machine — for example, the Teya Pro at £179 plus VAT. Teya is designed for quick setup with no long-term contract, so you can cancel anytime. Businesses with higher turnover can speak with a specialist for a custom plan.

**Q: What payment solutions does Teya offer?**

A: Teya offers a comprehensive suite of payment tools for small businesses: physical card terminals (including the Teya Pro), Teya Tap (turning a smartphone into a card machine), Pay by Link for remote payments, split-bill functionality, and 50+ EPOS integrations. All solutions support next-business-day or instant settlements and feed into a unified real-time sales dashboard via the Teya App.

---

*Generated by the GEO Audit Tool — read-only, additive recommendations only.*