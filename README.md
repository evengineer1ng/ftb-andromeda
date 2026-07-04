# From the Backmarker: Andromeda

A Starfield motorsport-ecosystem mod: careers, teams, sponsors, rivalries, championships, regional heat, hype, and emergent narrative — not a single race type. In the lineage of Night City Motorsports (Cyberpunk 2077, architecture reference only) and built directly on **FTB ("From the Backmarker")**, the author's own existing motorsport-management simulation, forked and re-themed for Starfield's Settled Systems rather than reinvented.

See `docs/ARCHITECTURE.md` and `docs/DECISIONS.md` for the full plan.

## Toolchain

- **Creative VM** (this repo's home): source of truth for all mod source — Papyrus scripts, xEdit-edited plugins, the forked/re-themed simulation (`sim/`), docs, build scripts. No local Starfield install by design; game files never live here.
- **Gaming VM**: the only place Starfield runs. Pulls this repo to author/test against live game data, pushes changes back. Toolchain there is deliberately minimal — xEdit (for quest/global/alias records) + a standalone Papyrus compiler + Mod Organizer 2. No Creation Kit install (see `docs/DECISIONS.md`, 2026-07-04). The simulation process (`sim/`) does **not** run here until commentary/live season tracking is deliberately turned on (see docs).
- **Bridge**: this GitHub repo. No direct VM-to-VM sharing — everything routes through commits/releases, on purpose, to force versioning discipline.
- **Distribution to Gaming VM's Mod Organizer 2**: build artifacts attached to GitHub Releases (tagged for milestones, a rolling pre-release for day-to-day iteration).

## Status

Foundation phase. No mod content yet. Next up: Phase 0 (toolchain proof) and Phase 0.5 (fork and stabilize the FTB simulation core, decoupled from its origin repo).
