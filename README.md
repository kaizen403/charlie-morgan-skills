# Charlie Morgan Skills

A Hermes / Claude-compatible **agent persona** that thinks, reasons, and coaches like Charlie Morgan — the British high-ticket consulting / agency-building practitioner behind Imperium Academy.

Built directly from 59 transcripts (~5.2MB / ~958,000 words) covering the full Imperium curriculum (week 1–6) plus 18 student case-study interviews.

## Repo layout

```
charlie-morgan-skills/
├── PERSONA.md                  # Top-level persona overview
├── instructions.md             # Runtime contract for the agent
├── style.md                    # Response formatting rules
├── profile/
│   ├── SOUL.md                 # Canonical identity
│   ├── voice.md                # Voice & language mechanics
│   ├── worldview.md            # Beliefs about reality, money, identity
│   └── operating_principles.md # Behavior rules
├── skills/                     # 36 detailed skill files (auto-load by topic)
└── Transcriptions/             # Source material — 59 transcripts
```

## Skills (36)

### Mindset / identity (week 1–2)

- `elucidatory-axioms-first-principles` — first-principles thinking framework
- `subjugating-reality` — radical responsibility
- `identity-ignition` — the identity-before-tactics premise
- `iterative-renaissance` — continuous self-rebuild loop
- `unrelenting-discipline` — discipline as the engine
- `six-figure-fusion` — holistic six-figure consulting blueprint
- `business-set-up` — operational shell of a consulting business
- `achieving-omniscience` — perception, awareness, mental models
- `oscillatory-life-cycles` — why people oscillate between drive and collapse
- `trial-by-fire` — the pain phases of identity change
- `polarity-paradoxes` — non-binary thinking, holding contradictions
- `designing-reality` — turning mindset into action via reverse-engineered plans

### Niche & offer (week 2–3)

- `niche-selection-grade-a` — grade-A niche selection criteria
- `niche-immersion-five-steps` — going deep enough to sell
- `offer-architecture-eight-steps` — outstanding offer construction
- `critical-information-overload` — radical research depth
- `critical-synthesising` — turning research into insight
- `defining-problem` — finding the *real* problem worth solving
- `mapping-methodology` — turning expertise into a transmittable system
- `iterative-expertise` — getting good through cycles, not study
- `guaranteeing-results` — designing meaningful guarantees
- `second-order-problems` — anticipating consequences of solutions

### Sales (week 4)

- `sales-bedrock` — the foundational sales worldview
- `imperium-conversion-playbook` — the full sales call structure
- `script-modification` — how to evolve the script as you sell
- `conquering-objections-vault` — exhaustive objection handling
- `oscillations-of-doubt` — reattaching prospect doubt after the call

### Acquisition (week 5)

- `appointments-fundamentals` — booking calls that actually convert
- `outbound-inbound-rulebook` — when to use which engine
- `asymmetric-psychological-leverage` — copy & persuasion psychology
- `building-outbound-systems` — cold email/DM/call architecture
- `building-inbound-systems` — content-driven inbound architecture
- `ninety-day-plan-of-attack` — aggressive 90-day acquisition sprint

### Operations (week 6)

- `virtual-assistant-masterclass` — hiring, training, managing VAs
- `team-management-basics` — first hires beyond VAs
- `client-onboarding-contracts` — onboarding sequences and contracts
- `managing-finances-cashflow` — separating money, paying yourself, taxes

### Synthesis

- `case-study-patterns` — meta-analysis of 18 student transformations

## How auto-loading works

Each `skills/<name>/SKILL.md` has a YAML frontmatter `description` field engineered to trigger on topic match. When the agent's runtime sees a task about (e.g.) "objection handling," it loads `conquering-objections-vault` automatically — no slash-command needed.

## License

All transcript content is © Charlie Morgan / Imperium Academy. This repository is a derivative analytical / training artifact intended for personal study and agent persona construction.

## Source

GitHub: https://github.com/kaizen403/charlie-morgan-skills (public)
