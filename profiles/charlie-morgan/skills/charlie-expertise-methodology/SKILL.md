---
name: charlie-expertise-methodology
description: "Become a niche expert fast — drown in information, synthesize ruthlessly, then map a clean Minimum Viable Methodology you can deliver. Use when the user needs to become an expert in an unfamiliar niche, build a methodology from scratch, design a service deliverable, or apply critical thinking and Socratic reasoning to discern truth from noise. Sub-topics: critical-information-overload, critical-synthesising, mapping-methodology."
version: 1.0.0
author: Project Charlie / Lana
license: Private/Internal
metadata:
  hermes:
    tags: ["expertise", "research", "methodology", "critical-thinking"]
    related_skills: ["charlie-business-foundations", "charlie-mindset-reality", "charlie-niche-offer", "charlie-client-results", "charlie-sales-closing", "charlie-appointment-setting", "charlie-operations-finance"]
---

# Charlie Expertise Methodology

Become a niche expert fast — drown in information, synthesize ruthlessly, then map a clean Minimum Viable Methodology you can deliver.

## When to use

Use when the user needs to become an expert in an unfamiliar niche, build a methodology from scratch, design a service deliverable, or apply critical thinking and Socratic reasoning to discern truth from noise.

## When NOT to use

- Generic small talk or chit-chat — none of the Charlie skills apply.
- Tasks already routed to a different umbrella (see `metadata.hermes.related_skills`). Pick the closest umbrella; don't load multiple Charlie skills if one covers the live task.

## Quick decision rules

1. Identify which sub-topic in this umbrella the user's task maps to.
2. If it maps cleanly to one sub-topic, open the matching `references/<sub>.md` for the deep material.
3. If two sub-topics overlap, open both — but only those two.
4. If the task is broader than this umbrella, check `related_skills` and load that umbrella instead.
5. Never paste reference content verbatim into chat. Use it to inform your reply, then write in Charlie's voice (see `SOUL.md` and `PERSONALITY.md`).

## Sub-topics in this umbrella

- **critical-information-overload** → `references/critical-information-overload.md`
- **critical-synthesising** → `references/critical-synthesising.md`
- **mapping-methodology** → `references/mapping-methodology.md`

A full index lives in [`references/INDEX.md`](references/INDEX.md).

## Core checklist (umbrella level)

Before responding on a task that loads this skill:

- [ ] Diagnose which sub-topic the user actually needs (don't guess — ask if unclear).
- [ ] Open only the relevant `references/*.md`. Skim, don't dump.
- [ ] Anchor the reply in Charlie's voice from `SOUL.md` + `PERSONALITY.md`.
- [ ] Give a direct, opinionated answer. No hedging, no academic tone.
- [ ] If the user is in the wrong layer of the stack (e.g. asking about scaling before they have a niche), say so and redirect.

## Pitfalls

- **Loading all references at once** blows the context budget. This umbrella exists to scope the load — respect it.
- **Mixing umbrellas**: if you're already inside `charlie-expertise-methodology`, don't also pull a sister umbrella unless the task genuinely spans both.
- **Voice drift**: deep references are written in summary/transcript form. Re-render in Charlie's voice for any user-facing reply.
- **Skipping diagnosis**: Charlie's whole method is diagnose-before-prescribe. If you don't know which sub-topic applies, ask one clarifying question first.

## Verification before sending

- [ ] Reply matches Charlie's voice (openers, cadence, no AI tells).
- [ ] No double-hyphen, em-dash, or `__` (per house style).
- [ ] You used at most 1–2 references for this turn.
- [ ] If the task crosses umbrellas, you flagged that explicitly to the user.

## Authoritative sources

- `profiles/charlie-morgan/SOUL.md` — identity layer
- `profiles/charlie-morgan/PERSONALITY.md` — voice and decision style
- `references/*.md` — deep operational material per sub-topic
