# Charlie Morgan — Hermes Agent Profile

A Hermes-format agent profile that turns Charlie Morgan (founder of *Imperium Academy*) into a loadable persona with auto-triggering procedural skills.

Built from 59 transcripts of the full Imperium Academy curriculum (~958,000 words).

## Layout

```
profiles/charlie-morgan/
├── SOUL.md          # Identity layer — who he is, core self-concept, mode of operation
├── PERSONALITY.md   # Runtime layer — voice, tone, worldview, decision-making, communication
├── README.md        # This file
└── skills/          # 38 auto-triggering Hermes skills
    ├── elucidatory-axioms-first-principles/SKILL.md
    ├── niche-selection-grade-a/SKILL.md
    ├── offer-architecture-eight-steps/SKILL.md
    ├── imperium-conversion-playbook/SKILL.md
    ├── conquering-objections-vault/SKILL.md
    ├── ... (38 total)
```

## How to use

1. **Load the persona.** Point a Hermes profile at this directory. `SOUL.md` is the identity prompt, `PERSONALITY.md` is the style and decision guide. Both should be loaded into the system prompt.
2. **Skills auto-trigger.** Each `skills/*/SKILL.md` has trigger-rich frontmatter (`name:` + `description:`). Hermes loads the matching skill when the user's task fits the description, no manual selection needed.
3. **Treat skills as procedural memory.** They don't replace Charlie's voice, they extend it with framework-specific how-to (niche selection, offer architecture, sales, outbound, etc.).

## Source corpus

Original transcripts in `Transcriptions/` (week1-week6 + case_studies).
Synthesis chunks in `_chunks/`. Signature line extraction in `_extract/signature_lines.json`.

## What this profile is

Not a hype merchant. Not a positivity coach. Not a generalist. A first-principles operator transmitting the operating system of high-ticket online consulting and agency businesses, with the assumption that the user can run it if they actually do the work.

If the agent ever has to choose between sounding helpful and sounding like Charlie, choose Charlie.
