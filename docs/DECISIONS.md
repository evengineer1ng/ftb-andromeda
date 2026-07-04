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

## 2026-07-04 — Phase 0.5 complete: FTB core vendored and proven standalone
Copied `ftb_game.py`/`ftb_names.py`/`ftb_race_day.py` from `F:\dev\oracle-radio\ftb_core\` into `sim/ftb_core/`, plus thin `sim/plugins/*.py` passthrough shims mirroring oracle-radio's own `plugins/` layout — this let all of `ftb_game.py`'s internal `from plugins.X import Y` lazy imports resolve unchanged, with zero edits to the vendored file itself. `sim/tests/test_ftb_core_standalone.py` proves `WorldBuilder.generate_world` + 14 days of `FTBSimulation.tick_simulation` run with no oracle-radio dependency (23 leagues, 18 tracks generated; 15k+ SimEvents over 14 days). Confirmed in passing: the `tkinter`/`customtkinter` UI section (SECTION 6) and the reference to a missing `plugins.ftb_heritage_templates` module are both already-optional/try-except-guarded in the source project itself — not something forking broke. Manufacturer/part generation currently no-ops as a result (heritage templates absent); writing Starfield-themed heritage templates is Phase 1 re-theming work regardless, so this isn't a new gap to fix, just one to fill on schedule.

## 2026-07-04 — Phase 1 re-theming started: manufacturers and tracks
Wrote `sim/starfield_theme/heritage_templates.py` (draft `HeritageTemplate`/`HERITAGE_TEMPLATES`/`get_weighted_template`, wired in via `sim/plugins/ftb_heritage_templates.py`) to fill the manufacturer/part generation gap found in Phase 0.5 — 5 invented archetypes (United Colonies/Freestar Frontier/Crimson Salvage/Ryujin Precision/Deep Frontier Independent), explicitly not lifted from specific in-lore corporations; soft sponsor ties to real Starfield factions remain a separate later layer. Verified: 17 manufacturers/582 parts now generate with names like "Vanguard Industries," "Akila Outfitters," "Nova Foundry."

Also edited `sim/ftb_core/ftb_names.py`'s `TRACK_LOCATIONS` directly (real-world-city block replaced with Starfield/invented settlement names) — this is a real edit to the vendored file, not a passthrough shim, since these are hardcoded module constants rather than an importable plugin. A handful of the new names (New Atlantis, Akila, Neon, Cydonia, Paradiso, The Well, Jemison, Gagarin, Porrima, Volii) are asserted as real in-lore locations but not independently verified — check against actual game knowledge before treating as canon. The rest are invented frontier/settlement names in the same spirit as the file's pre-existing "Fictional/Atmospheric locations" block.

## 2026-07-03 — No Starfield install on the Creative VM
Deliberate: forces all mod content through git rather than blurring authoring and testing, and is a forcing function for commit discipline.
