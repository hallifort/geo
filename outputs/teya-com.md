# GEO Audit Report — teya.com

**URL:** https://teya.com  
**Business type:** SaaS  
**Audited:** 2026-06-08 22:39 UTC  
**GEO Score:** 🔴 22/100

---

## Executive Summary

Teya's homepage communicates its value proposition clearly in human-readable copy but is critically under-structured for AI engines: no detectable JSON-LD schema, weak entity disambiguation, and no FAQ markup. AI models attempting to cite Teya for payment-solution or small-business queries have little machine-readable signal to latch onto, leaving the site vulnerable to being overlooked in favour of better-structured competitors.

---

## Schema.org Coverage

**Present:** None detected

**Missing / recommended:**
- `Organization`
- `WebSite`
- `FAQPage`
- `Product`
- `FinancialProduct`
- `SoftwareApplication`
- `Review`
- `AggregateRating`
- `BreadcrumbList`
- `ItemList`

---

## Entity & Authority Signals

| Signal | Assessment |
|--------|------------|
| Organisation identity | Weak. The company name 'Teya' appears throughout, but there is no structured description of what Teya is as a legal entity, when it was founded (2019 is mentioned), where it is headquartered, or what regulatory body oversees it. AI engines cannot confidently resolve 'Teya' as a distinct, authoritative entity. |
| sameAs links | Absent. No links to Wikidata, LinkedIn, Companies House, Crunchbase, or social profiles are present in the scraped content, making cross-platform entity reconciliation impossible for knowledge-graph-based AI systems. |
| Authority markers | Partial. The Trustpilot rating (4.3/5 from 1,270 reviews) and customer count (75,000+ active members) are present in copy but not encoded in structured data. Regulatory or financial-licence credentials are not mentioned, which is a significant gap for a fintech SaaS. |

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
| What is Teya? | ⚠️ partially-covered | The headline and subheadline describe the product suite but there is no concise, citable one-paragraph definition of Teya as a company — no founding story, legal category, or mission statement in structured form. |
| What payment solutions does Teya offer? | ⚠️ partially-covered | Card machines, Tap-to-pay, Pay by Link, Business Account, and Cash Advance are all named in copy, but they are not enumerated in a machine-readable list or structured product schema that AI engines can extract reliably. |
| How does Teya help small businesses? | ⚠️ partially-covered | Customer testimonials and feature bullets address this, but the answer is spread across carousel and marquee elements that are difficult for AI scrapers to parse coherently. |
| What are Teya's fees? | ⚠️ partially-covered | The 'Start' plan rate of 1.59% for consumer cards and the £29.99 low-turnover fee are visible in copy, but no complete fee table is encoded in structured data, and higher-tier plan rates are truncated. |
| Is Teya available in my country? | ❌ not-covered | No geographic availability, supported countries, or areaServed information appears anywhere in the scraped content. |
| How do I sign up for Teya? | ❌ not-covered | CTAs like 'Join Us' and 'Check our offers' exist but there is no step-by-step onboarding description or structured HowTo/signup flow that AI engines could summarise. |

---

## Recommended JSON-LD Additions

> Paste each block inside a `<script type="application/ld+json">` tag in your `<head>`.  
> These are purely additive — they do not change any existing HTML, CSS, or copy.

### Addition 1 — 🔴 High Priority

**Gap addressed:** Core Organisation identity with founding date, description, area served, aggregate rating, and sameAs links — the single highest-impact fix for AI entity resolution

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Teya",
  "url": "https://www.teya.com",
  "foundingDate": "2019",
  "description": "Teya is a fintech company founded in 2019 that provides integrated payment solutions, business accounts, and funding products designed specifically for small and local businesses. Its product suite includes card machines, Tap-to-Pay, Pay by Link, a Business Debit Account with 0.5% cashback, and a Cash Advance facility.",
  "slogan": "Empowering local businesses to thrive",
  "areaServed": {
    "@type": "Country",
    "name": "United Kingdom"
  },
  "numberOfEmployees": {
    "@type": "QuantitativeValue",
    "minValue": 100
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.3",
    "bestRating": "5",
    "ratingCount": "1270",
    "reviewCount": "1270"
  },
  "sameAs": [
    "https://uk.trustpilot.com/review/teya.com",
    "https://www.linkedin.com/company/teya",
    "https://twitter.com/teya"
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

**Gap addressed:** FAQPage schema covering the most-searched questions about Teya that are currently not-covered or only partially covered — directly boosts AI Overview and People Also Ask citation likelihood

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
        "text": "Teya is a UK-based fintech company founded in 2019 that offers integrated payment, banking, and funding solutions for small and local businesses. Its platform combines card machines, a Business Account with 0.5% cashback, Pay by Link, Tap-to-Pay, real-time sales tracking, and Cash Advance funding \u2014 all managed through a single app. Teya is trusted by over 75,000 active business members."
      }
    },
    {
      "@type": "Question",
      "name": "Is Teya available in my country?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya's primary market is the United Kingdom, where its card machines, Business Account, and Cash Advance products are available to small businesses. Businesses outside the UK should contact Teya directly via teya.com to enquire about availability in their region."
      }
    },
    {
      "@type": "Question",
      "name": "How do I sign up for Teya?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "To sign up for Teya, visit teya.com/pricing to select a membership plan based on your monthly card turnover. Plans start from 1.59% on consumer card transactions. Choose a card machine, complete the online application, and Teya's team will support you through setup. There are no long-term contracts \u2014 you can cancel anytime."
      }
    },
    {
      "@type": "Question",
      "name": "What are Teya's fees?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya uses a transparent, plan-based pricing model. The 'Start' plan charges 1.59% on consumer card transactions for businesses with monthly card turnover up to \u00a37,500. A \u00a329.99 monthly fee applies if card turnover falls below \u00a32,500. Teya advertises simple rates, no hidden fees, and next-day settlements. For higher-turnover businesses, custom plans are available."
      }
    }
  ]
}
</script>
```

### Addition 3 — 🟡 Medium Priority

**Gap addressed:** SoftwareApplication / FinancialProduct ItemList to describe Teya's product suite in a machine-readable format, enabling AI engines to enumerate and compare Teya's offerings accurately

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Teya Payment and Business Solutions",
  "description": "Teya's integrated suite of payment, account, and funding products for small businesses.",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Product",
        "name": "Teya Card Machines",
        "description": "In-person payment terminals including Teya Pro and other models with built-in calculator, tipping, split-bill, and lifetime warranty. Transactions settle next business day or instantly (subject to eligibility).",
        "url": "https://www.teya.com/card-machines",
        "brand": {
          "@type": "Brand",
          "name": "Teya"
        }
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@type": "Product",
        "name": "Teya Business Account",
        "description": "A business debit account with 0.5% cashback on all spending, the ability to create multiple cards with individual limits, and seamless integration with Teya card machine settlements.",
        "url": "https://www.teya.com/business-account",
        "brand": {
          "@type": "Brand",
          "name": "Teya"
        }
      }
    },
    {
      "@type": "ListItem",
      "position": 3,
      "item": {
        "@type": "Product",
        "name": "Teya Cash Advance",
        "description": "Flexible business funding repaid automatically as a percentage of daily card machine sales. Over \u00a368,000,000 advanced to date. Designed for small businesses needing fast, transparent capital without fixed monthly repayments.",
        "url": "https://www.teya.com/funding",
        "brand": {
          "@type": "Brand",
          "name": "Teya"
        }
      }
    },
    {
      "@type": "ListItem",
      "position": 4,
      "item": {
        "@type": "Product",
        "name": "Teya Tap",
        "description": "A mobile app that turns an iPhone or Android smartphone into a contactless card machine, allowing businesses to accept tap-to-pay payments without dedicated hardware.",
        "brand": {
          "@type": "Brand",
          "name": "Teya"
        }
      }
    },
    {
      "@type": "ListItem",
      "position": 5,
      "item": {
        "@type": "Product",
        "name": "Pay by Link",
        "description": "Remote payment solution enabling businesses to send payment links to customers and get paid at a distance, with funds settled next business day.",
        "brand": {
          "@type": "Brand",
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

A: Teya currently operates primarily in the United Kingdom, serving over 75,000 small and local businesses with its card machines, Business Account, and Cash Advance products. Businesses outside the UK should visit teya.com or contact the sales team directly to check availability in their country.

**Q: How do I sign up for Teya?**

A: Signing up for Teya starts at teya.com/pricing, where you select a membership plan based on your monthly card turnover. The entry-level Start plan covers turnover up to £7,500 at 1.59% on consumer cards. After choosing a plan and a card machine, you complete an online application — setup is described as quick, and there are no long-term contracts, so you can cancel at any time.

**Q: What payment solutions does Teya offer?**

A: Teya offers a fully integrated suite of payment tools: physical card terminals (including the Teya Pro with a built-in printer), Teya Tap (which turns your smartphone into a card machine), Pay by Link for remote payments, split-bill functionality, and 50+ EPOS integrations. All solutions feed into the Teya App for real-time sales tracking, and funds can settle next business day or instantly (subject to eligibility).

---

*Generated by the GEO Audit Tool — read-only, additive recommendations only.*