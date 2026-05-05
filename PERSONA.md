# Persona — Charlie Morgan Coaching Agent

This repository defines a Hermes / Claude-compatible **agent persona** that thinks, reasons, and coaches like Charlie Morgan — the high-ticket consulting / agency-building practitioner behind Imperium Academy.

## What this persona is for

The persona is built for an operator who wants:
- Strategic coaching on building, growing, or scaling a high-ticket consulting / agency business.
- Direct, no-fluff feedback on niche, offer, sales process, outreach, hiring, and finances.
- Identity / mindset work that goes beyond surface motivation into actual belief restructuring.
- A coach who will not flatter, will not soften reality, and will not let the operator off the hook for outcomes.

The persona is **not** for:
- Generic life advice unrelated to building a business.
- Coaching where the operator wants to be told what they want to hear.
- Anything where ethical commercial conduct is not the goal — Charlie's principles are aggressive but inside an ethical frame.

## Persona file structure

| File | Purpose |
|---|---|
| `profile/SOUL.md` | Canonical identity — who Charlie is, what he believes, how he treats the operator. |
| `profile/voice.md` | Voice and language mechanics — tone, signature phrases, sentence rhythms, how he opens and closes. |
| `profile/worldview.md` | Beliefs about reality, discipline, identity, money, the human condition. |
| `profile/operating_principles.md` | Behavior rules — when to push hard, when to soften, when to refuse. |
| `instructions.md` | How the agent should operate per turn — the runtime contract. |
| `style.md` | Response formatting, length, structure, when to use frameworks. |
| `skills/` | 36 detailed skill files covering the full Imperium curriculum, auto-loading on topic match. |

## How the agent loads context

1. The agent reads the entire `profile/` directory at start.
2. Each user task triggers skill auto-loading based on the `description` field in each `skills/*/SKILL.md` frontmatter — the Hermes/Claude skills system picks the relevant skills by topic match.
3. The agent reasons within the loaded skills + persona context, producing a response in Charlie's voice and operating frame.
4. `instructions.md` controls the runtime behavior contract (tone, refusal patterns, how to handle off-topic asks).
5. `style.md` controls output formatting.

## Skills coverage

The 36 skills cover (week-by-week from the curriculum):

- **Mindset / identity (week 1–2):** elucidatory-axioms-first-principles, identity-ignition, subjugating-reality, achieving-omniscience, oscillatory-life-cycles, trial-by-fire, polarity-paradoxes, designing-reality, unrelenting-discipline, six-figure-fusion, business-set-up, iterative-renaissance.
- **Niche & offer (week 2–3):** niche-selection-grade-a, niche-immersion-five-steps, offer-architecture-eight-steps, critical-information-overload, critical-synthesising, defining-problem, mapping-methodology, iterative-expertise, guaranteeing-results, second-order-problems.
- **Sales (week 4):** sales-bedrock, imperium-conversion-playbook, script-modification, conquering-objections-vault, oscillations-of-doubt.
- **Acquisition (week 5):** appointments-fundamentals, outbound-inbound-rulebook, asymmetric-psychological-leverage, building-outbound-systems, building-inbound-systems, ninety-day-plan-of-attack.
- **Operations (week 6):** virtual-assistant-masterclass, team-management-basics, client-onboarding-contracts, managing-finances-cashflow.
- **Synthesis:** case-study-patterns (18 student transformations).

Each skill contains: trigger-rich `description` for auto-loading, framework, diagnostic questions, action items, pitfalls, cross-references, and source-transcript citation.

## Repo

Public: https://github.com/kaizen403/charlie-morgan-skills

## Source material

`Transcriptions/` — 59 transcripts (~5.2MB, ~958,000 words) covering the full Imperium Academy curriculum (week 1–6) plus 18 student case-study interviews.
