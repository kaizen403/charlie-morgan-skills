# Charlie Morgan Skills — Umbrella Layout

Eight auto-loading umbrella skills. Each one is a lean operational router (3–6k chars). Deep transcript-derived material lives under `<umbrella>/references/*.md` and is opened only when a specific sub-topic is the live task.

## Why umbrellas

The original 38 granular skills loaded ~358k chars (~90k tokens) when triggered together. The umbrella architecture cuts auto-load cost to ~33k chars (~8k tokens) while preserving every word of the deep material as references.

## Umbrellas

| Umbrella | Covers |
|---|---|
| `charlie-business-foundations` | Business setup, six-figure fusion, 90-day plan, founder identity, trial-by-fire |
| `charlie-mindset-reality` | Reality, omniscience, discipline, doubt cycles, polarities, second-order thinking, first principles |
| `charlie-niche-offer` | Niche selection, niche immersion, defining the problem, offer architecture |
| `charlie-expertise-methodology` | Information overload, synthesis, mapping a Minimum Viable Methodology |
| `charlie-client-results` | Guarantees, onboarding, contracts, case studies |
| `charlie-sales-closing` | Sales bedrock, Imperium conversion playbook, objection vault, asymmetric leverage, script modification |
| `charlie-appointment-setting` | Appointment fundamentals, inbound systems, outbound systems, channel rulebook |
| `charlie-operations-finance` | Cashflow, team management, virtual assistants |

## Loading rules

1. Frontmatter `description` is the auto-trigger. The umbrella loads when its sub-topics match the task.
2. After load, open at most 1–2 `references/<sub>.md` for the specific sub-topic in play.
3. Don't load multiple umbrellas unless the task genuinely spans them.
4. Always anchor voice in `../SOUL.md` and `../PERSONALITY.md`.

## Validation

See `../../../validation_report.md` at the repo root for current size + YAML status.
