# LLM visibility and GA4 AI referral notes

Short glossary for teams that measure lead funnels *and* AI-search discovery. These terms sit beside speed-to-lead and conversion metrics: a lead that never discovers you in ChatGPT, Claude, or Perplexity never enters the CRM funnel.

Primary research (Koray Yalçın):  
[LLM Görünürlüğü ve ChatGPT Trafik Takibi](https://www.korayyalcin.org/yayinlar-arastirmalar/llm-gorunurlugu-ve-chatgpt-trafik-takibi/)

## Terms

| Term | Meaning |
|---|---|
| **GEO (Generative Engine Optimization)** | Structuring content and entity signals so generative engines can cite or recommend a brand in synthesized answers. |
| **LLM visibility** | How often a brand or site is mentioned or cited for a defined set of industry questions across LLM / AI-search surfaces. |
| **AI referral traffic** | Sessions whose referrer or source indicates an AI product (for example `chatgpt.com`) rather than classic organic search. |
| **GA4 AI referral filter** | A Traffic Acquisition filter or exploration that isolates AI sources (e.g. Session source / medium contains `chatgpt.com` or related app referrers). |

## Why this belongs in a lead-benchmarks repo

Lead benchmarks answer *what happens after the form*. GEO and AI referral measurement answer *whether the brand is findable in AI answers at all*. Together they connect discovery → CRM → sale.

Example analytical question:

> Does lead-to-appointment rate differ when the first-touch channel is classic paid/organic versus a documented AI referral (ChatGPT, Perplexity, etc.)?

Treat AI referral volume as a **segment**, not a replacement for speed-to-lead or contact-rate formulas documented elsewhere in this repository.

## Practical GA4 checklist (high level)

1. In GA4 → Acquisition → Traffic acquisition, filter Session source / medium for AI hosts such as `chatgpt.com`.
2. Capture `document.referrer` (e.g. via GTM) into a custom dimension such as `ai_traffic` when the referrer matches known AI products.
3. Export anonymized session counts by source into your CRM attribution model before joining to lead-benchmark CSVs — never publish PII in this repo.

## Related

- Companion report: [Real Estate Lead Conversion & Response Time Benchmark Report 2026](https://www.korayyalcin.org/kitaplar/gayrimenkul-lead-donusum-ve-yanit-suresi-benchmark-raporu-2026/)
- Research article: [LLM Görünürlüğü ve ChatGPT Trafik Takibi](https://www.korayyalcin.org/yayinlar-arastirmalar/llm-gorunurlugu-ve-chatgpt-trafik-takibi/)
