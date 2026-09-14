# Benchmark Methodology

This document defines how real estate lead benchmarks should be calculated and reported.

## 1. Define the population

Before calculating any KPI, document:

- date range
- geography
- lead sources
- campaigns included
- projects included
- whether reactivated leads are included
- whether duplicate leads are included
- whether test leads are excluded

## 2. Use a stable lead identifier

Each lead should have one anonymous internal identifier. Public datasets should never expose CRM IDs if those IDs can be linked back to a person.

## 3. Normalize timestamps

All timestamps should use a single timezone or ISO 8601 with timezone information.

Minimum timestamps:

- `lead_created_at`
- `first_attempt_at`
- `first_contacted_at`
- `qualified_at`
- `appointment_created_at`
- `appointment_completed_at`
- `won_at`
- `lost_at`

## 4. Define contact consistently

A lead should be marked `contacted=true` only when two-way communication is established. A dial attempt, delivered WhatsApp message or sent e-mail alone should not count as successful contact.

## 5. Define qualification consistently

A qualified lead should satisfy the team's documented criteria. Typical fields include budget, purchase timing, preferred location/project, property type and intent.

## 6. Define appointments consistently

Distinguish between:

- scheduled appointment
- completed appointment
- cancelled appointment
- no-show

Do not use one generic appointment field when calculating show-up rate.

## 7. Response time

`speed_to_lead_minutes = first_attempt_at - lead_created_at`

Track at least:

- median
- p75
- p90
- response-time bands
- missing first-attempt timestamps

Averages alone can be distorted by extreme delays.

## 8. Funnel denominators

Always state the denominator.

Examples:

- Contact Rate = contacted / total leads
- Qualification Rate = qualified / contacted
- Appointment Rate (contacted basis) = appointments / contacted
- Appointment Rate (qualified basis) = appointments / qualified
- Show-up Rate = completed appointments / scheduled appointments
- Lead-to-Sale = won / total leads
- Contact-to-Sale = won / contacted

Two teams can report different values for the same named KPI if denominators differ.

## 9. Segment before interpreting

Recommended cuts:

- source
- campaign
- project
- market
- language
- sales rep
- response-time band
- lead score
- month / week

## 10. Missing data

Report missing-data rates for critical fields. Do not silently treat missing timestamps as zero-minute response times or missing outcomes as lost deals.

## 11. Outliers

Keep raw outliers in source data, but report robust statistics such as median and percentiles. Clearly document any exclusions.

## 12. Privacy

Public examples must be synthetic, aggregated or irreversibly anonymized. Do not publish names, phone numbers, e-mails, message text or direct CRM identifiers.

## 13. Reproducibility

A benchmark publication should include:

- methodology version
- metric definitions
- data dictionary
- sample size
- date range
- segmentation rules
- known limitations

This allows future updates to be compared consistently.
