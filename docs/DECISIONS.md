# Decisions (ADR-style log)

## 2026-07-03 — Project renamed vector-circuit → From the Backmarker: Andromeda (slug `ftb-andromeda`)
After discovering the actual scale of FTB (`F:\dev\oracle-radio\ftb_core\ftb_game.py`), the project leans directly on its roots rather than treating it as loose inspiration.

## 2026-07-03 — Vendor/fork FTB's code rather than reinvent it
FTB v1's entity model (Driver/Engineer/Mechanic/Strategist/Car/Manufacturer/Part/Contract/Sponsorship/Budget/League/FreeAgent) already matches the career/team/sponsor/contract ecosystem this mod wants. Forking and re-theming is less work and more depth than building an equivalent from scratch. Decoupled from oracle-radio's ongoing development (no live import dependency) since oracle-radio is under active, unrelated change (an in-progress LLM-narration-to-grammar pivot noted in its own docs).

## 2026-07-03 — Native SFSE/C++ plugin work is a planned track, not a deferred risk
SFSE is pre-alpha and Cassiopeia Papyrus Extender's ~430 functions are the current ceiling for pure-Papyrus ship hooks. Earlier planning drafts scoped deep ship AI out entirely; revised because the author is willing to do native plugin engineering. Still sequenced after Phase 2's time-trial proof, so a fast win isn't blocked on the native track's timeline.

## 2026-07-03 — Sim process stays off the Gaming VM until commentary/live tracking is wanted
Keeps the Gaming VM as a clean game+MO2 environment for now. Means Phase 0-4's sim work is verified against fixture/hand-copied logs, not live gameplay data, and Phase 1's in-game reward logic is temporarily self-contained in Papyrus rather than depending on a live round-trip.

## 2026-07-03 — Phase 1 is solo time-trial, not AI opponents
No precedent exists for AI-driven rover opponents in Starfield. Treated as its own future feasibility spike rather than a Phase 1 blocker.

## 2026-07-03 — No Starfield install on the Creative VM
Deliberate: forces all mod content through git rather than blurring authoring and testing, and is a forcing function for commit discipline.
