# Data Dictionary

Recommended fields for reproducible real estate lead benchmark analysis.

| Field | Type | Description |
|---|---|---|
| `lead_id` | string | Anonymous unique lead identifier |
| `lead_created_at` | datetime | CRM creation timestamp |
| `first_attempt_at` | datetime | First logged outbound attempt |
| `first_contacted_at` | datetime | First successful two-way contact |
| `qualified_at` | datetime | Qualification timestamp |
| `appointment_created_at` | datetime | Appointment scheduled timestamp |
| `appointment_completed_at` | datetime | Appointment completion timestamp |
| `won_at` | datetime | Won/sale timestamp |
| `lost_at` | datetime | Lost timestamp |
| `source` | string | Lead source, e.g. meta_ads, google_ads, portal |
| `campaign` | string | Campaign name or anonymous campaign key |
| `project` | string | Project or portfolio key |
| `market` | string | Country/market |
| `language` | string | Lead language |
| `sales_rep` | string | Anonymous sales-rep identifier |
| `contacted` | boolean | Two-way communication established |
| `qualified` | boolean | Qualification criteria met |
| `appointment_scheduled` | boolean | Appointment scheduled |
| `appointment_completed` | boolean | Appointment occurred |
| `won` | boolean | Lead converted to sale |
| `lost` | boolean | Lead closed as lost |
| `lost_reason` | string | Standardized lost reason |
| `lead_score` | number | Optional lead score |
| `media_spend_allocated` | number | Optional attributed media spend |

## Derived fields

These fields can be calculated rather than stored:

- `speed_to_lead_minutes`
- `response_time_band`
- `days_to_contact`
- `days_to_appointment`
- `days_to_sale`

## Recommended controlled values

### source

`meta_ads`, `google_ads`, `website`, `portal`, `whatsapp`, `referral`, `organic`, `offline`, `other`

### lost_reason

`no_response`, `budget`, `timing`, `location`, `project_mismatch`, `financing`, `competitor`, `duplicate`, `invalid`, `not_interested`, `other`

## Privacy rule

Do not include names, phone numbers, e-mail addresses or free-text conversation content in public benchmark datasets.
