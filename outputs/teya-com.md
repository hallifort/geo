# GEO Audit Report — teya.com

**URL:** https://teya.com  
**Business type:** SaaS  
**Audited:** 2026-06-08 23:07 UTC  
**GEO Score:** 🔴 22/100

---

## Executive Summary

Teya's homepage has strong on-page copy but almost no structured data, making it difficult for AI engines to extract and cite key facts about the company, its products, or its pricing. Critical entity signals such as founding year, geographic availability, and explicit fee structures are either absent or buried in unstructured text. Adding JSON-LD schema and a concise FAQ block would meaningfully improve Teya's chances of being surfaced in AI-generated answers about payment solutions for small businesses.

---

## Schema.org Coverage

**Present:** None detected

**Missing / recommended:**
- `Organization`
- `FinancialProduct`
- `FAQPage`
- `Product`
- `AggregateRating`
- `WebSite`
- `SiteLinksSearchBox`

---

## Entity & Authority Signals

| Signal | Assessment |
|--------|------------|
| Organisation identity | Teya is identified by name and a broad tagline ('Empowering local businesses to thrive') but no formal legal entity name, registered address, regulatory status, or founding story is surfaced in structured form. The founding year 2019 appears only in a heading. |
| sameAs links | No sameAs links to LinkedIn, Companies House, Crunchbase, Wikipedia, or social profiles are present in the scraped content, significantly weakening cross-platform entity disambiguation for AI engines. |
| Authority markers | A Trustpilot rating of 4.3/5 from 1,270 reviews is referenced, and customer testimonials are included, but these are rendered as widget content rather than machine-readable structured data. Regulatory/licensing credentials are not mentioned. |

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
| What is Teya? | ⚠️ partially-covered | The homepage describes Teya's value proposition but provides no concise, citable definition of what Teya is as a company — no legal status, regulatory context, or one-sentence description suitable for AI extraction. |
| What payment solutions does Teya offer? | ⚠️ partially-covered | Products like card machines, Teya Tap, Pay by Link, and Business Account are mentioned but not described in a structured, enumerable format that AI engines can easily lift and cite. |
| How does Teya help small businesses? | ⚠️ partially-covered | Benefits are listed (next-day settlements, no hidden fees, Cash Advance, etc.) but are fragmented across bullet lists and testimonials without a single authoritative summary passage. |
| What are Teya's fees? | ⚠️ partially-covered | The Start plan rate of 1.59% for consumer cards is visible, and a £29.99 monthly fee condition is mentioned, but full fee tables are truncated and not machine-readable. |
| Is Teya available in my country? | ❌ not-covered | No geographic availability information is present on the homepage. UK context is implied by testimonials and GBP pricing but never explicitly stated. |
| How do I sign up for Teya? | ❌ not-covered | CTAs like 'Join Us' and 'Check our offers' exist but no step-by-step sign-up process or eligibility criteria are described anywhere in the scraped content. |

---

## Recommended JSON-LD Additions

> Paste each block inside a `<script type="application/ld+json">` tag in your `<head>`.  
> These are purely additive — they do not change any existing HTML, CSS, or copy.

### Addition 1 — 🔴 High Priority

**Gap addressed:** No Organization schema — AI engines cannot reliably identify Teya as a distinct entity with verifiable attributes

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Teya",
  "url": "https://www.teya.com",
  "logo": "https://www.teya.com/favicon.ico",
  "foundingDate": "2019",
  "description": "Teya is a financial technology company founded in 2019 that provides integrated payment solutions, business accounts, and funding products to small and local businesses. Teya serves over 75,000 active members and has processed more than 609 million transactions in 2025.",
  "areaServed": {
    "@type": "Country",
    "name": "United Kingdom"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.3",
    "reviewCount": "1270",
    "bestRating": "5",
    "worstRating": "1"
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

**Gap addressed:** No FAQPage schema — top questions about Teya's products, fees, availability, and sign-up process are not machine-readable

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
        "text": "Teya is a financial technology company founded in 2019 that offers integrated payments, business accounts, and funding solutions designed specifically for small and local businesses. Trusted by over 75,000 customers, Teya provides card machines, a business debit account with 0.5% cashback, Pay by Link, and Cash Advance funding, all managed through a single app."
      }
    },
    {
      "@type": "Question",
      "name": "What payment solutions does Teya offer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya offers a range of payment solutions including physical card terminals (Teya Pro and other models), Teya Tap (which turns a smartphone into a card machine), Pay by Link for remote payments, a Business Account with a debit card, and Cash Advance funding. All products integrate with 50+ EPOS systems and are managed via the Teya App."
      }
    },
    {
      "@type": "Question",
      "name": "What are Teya's fees?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya's pricing is based on monthly card turnover. The Start plan, for businesses with up to \u00a37,500 monthly card turnover, charges 1.59% on consumer card transactions. A \u00a329.99 monthly fee applies when monthly card turnover is under \u00a32,500. Teya advertises no hidden fees and offers simple, transparent rates. Custom plans are available for higher-volume businesses."
      }
    },
    {
      "@type": "Question",
      "name": "Is Teya available in my country?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya primarily serves businesses in the United Kingdom. Pricing is listed in GBP and customer support is UK-based. Businesses outside the UK should contact Teya directly to confirm availability in their region."
      }
    },
    {
      "@type": "Question",
      "name": "How do I sign up for Teya?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "To sign up for Teya, visit teya.com/pricing to select a membership plan based on your monthly card turnover, choose a card machine, and complete the online registration. Setup is described as quick, and Teya offers next-day settlements once your account is active. High-volume businesses can speak with a specialist for a custom plan."
      }
    },
    {
      "@type": "Question",
      "name": "How does Teya help small businesses?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Teya helps small businesses by combining payments, a business account, and funding into one integrated platform. Key benefits include next-day settlements, instant settlement eligibility, a 0.5% cashback debit card, Cash Advance funding repaid directly from card sales, real-time sales tracking, 50+ EPOS integrations, and a lifetime warranty on card machines \u2014 all with no hidden fees and human customer support."
      }
    }
  ]
}
</script>
```

### Addition 3 — 🟡 Medium Priority

**Gap addressed:** No FinancialProduct or SoftwareApplication schema — Teya's core product offerings are invisible to AI knowledge graphs

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Teya Payment Solutions",
  "description": "Integrated payment and financial management products offered by Teya for small businesses in the UK.",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Product",
        "name": "Teya Pro Card Machine",
        "description": "A premium card terminal with longer battery life and built-in printer, designed for small businesses. Supports contactless, chip-and-pin, and split-bill payments.",
        "offers": {
          "@type": "Offer",
          "price": "179",
          "priceCurrency": "GBP",
          "availability": "https://schema.org/InStock",
          "seller": {
            "@type": "Organization",
            "name": "Teya"
          }
        }
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@type": "SoftwareApplication",
        "name": "Teya Tap",
        "applicationCategory": "FinanceApplication",
        "operatingSystem": "iOS, Android",
        "description": "Teya Tap turns a smartphone into a contactless card machine, allowing businesses to accept tap-to-pay payments without dedicated hardware.",
        "offers": {
          "@type": "Offer",
          "seller": {
            "@type": "Organization",
            "name": "Teya"
          }
        }
      }
    },
    {
      "@type": "ListItem",
      "position": 3,
      "item": {
        "@type": "FinancialProduct",
        "name": "Teya Cash Advance",
        "description": "A flexible business funding product for Teya customers, repaid automatically as a percentage of daily card machine sales. Over \u00a368,000,000 in total Cash Advance has been provided to UK small businesses.",
        "provider": {
          "@type": "Organization",
          "name": "Teya"
        },
        "areaServed": {
          "@type": "Country",
          "name": "United Kingdom"
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

A: Teya primarily operates in the United Kingdom, where its card machines, Business Account, and Cash Advance products are available. All pricing is in GBP and customer support is UK-based. Businesses outside the UK should contact Teya directly at teya.com to check availability in their region.

**Q: How do I sign up for Teya?**

A: Signing up for Teya starts at teya.com/pricing, where you select a membership plan based on your monthly card turnover and choose a card machine. The setup process is designed to be quick, with no lengthy contracts — Teya operates on a cancel-anytime model. High-volume businesses can request a custom plan by speaking with a Teya specialist.

**Q: What payment solutions does Teya offer?**

A: Teya offers physical card terminals (including the Teya Pro with a built-in printer), Teya Tap (which turns any smartphone into a contactless card reader), Pay by Link for remote and online payments, and a Business Account debit card with 0.5% cashback. All products connect to 50+ EPOS systems and are managed through the Teya App, which provides real-time sales tracking and expense management.

---

*Generated by the GEO Audit Tool — read-only, additive recommendations only.*