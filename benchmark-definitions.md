# Benchmark Definitions

A benchmark is only useful when the metric definition is stable.

## Core funnel

`Lead → Attempted → Contacted → Qualified → Appointment → Show-up → Won`

## Lead
A unique, valid inquiry entering the CRM during the analysis period.

## Attempted
At least one outbound contact attempt was logged.

## Contacted
Two-way communication was established through phone, WhatsApp, SMS, e-mail or another approved channel.

## Qualified
The lead met the organization's documented qualification criteria.

## Appointment
A meeting, call, office visit, site visit or online presentation was scheduled.

## Show-up
The scheduled appointment actually took place.

## Won
The opportunity reached the organization's documented sale/completion stage.

## Lost
The opportunity was closed with a documented lost reason.

## No Response
The lead received one or more contact attempts but no two-way communication was established.

## Speed-to-Lead
Minutes between lead creation and the first human or qualifying automated contact attempt, depending on the benchmark definition being used. The chosen definition must be disclosed.

## Contact Rate
`contacted_leads / total_valid_leads`

## Qualification Rate
Recommended default:
`qualified_leads / contacted_leads`

Alternative denominators are acceptable only when clearly labeled.

## Appointment Rate
Two useful versions:

- Contacted-basis: `appointments / contacted_leads`
- Qualified-basis: `appointments / qualified_leads`

## Show-up Rate
`completed_appointments / scheduled_appointments`

## Lead-to-Sale Conversion
`won_leads / total_valid_leads`

## Contact-to-Sale Conversion
`won_leads / contacted_leads`

## CPL
`media_spend / total_valid_leads`

## Cost per Contact
`media_spend / contacted_leads`

## Cost per Appointment
`media_spend / scheduled_appointments`

## Cost per Sale
`media_spend / won_leads`

## Important rule
Never compare two benchmark values unless their denominator, sample definition and time period are compatible.
