# Speed-to-Lead

Speed-to-Lead measures the delay between lead creation and the first recorded contact attempt.

## Formula

`first_attempt_at - lead_created_at`

## Recommended reporting

Report:

- median
- p75
- p90
- percentage with no attempt recorded
- response-time distribution

## Suggested analysis bands

- 0–5 minutes
- 6–15 minutes
- 16–30 minutes
- 31–60 minutes
- 1–4 hours
- 4–24 hours
- 24+ hours
- no attempt recorded

These are analysis bands, not claimed universal industry standards.

## Why median matters

Averages can be distorted by a small number of very late responses. Median and percentiles better show operational consistency.

## Useful comparison

Compare Contact Rate, Appointment Rate and Lead-to-Sale Conversion by response-time band.

## Data quality checks

Flag:

- first attempt before lead creation
- missing lead creation timestamp
- missing first attempt
- impossible timezone differences
- duplicated lead records
