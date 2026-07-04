# Architecture

## Two-VM split

- **Creative VM**: all authoring — Papyrus source, xEdit-managed plugin project, the `sim/` simulation, docs, build scripts. No Starfield install here, by design.
- **Gaming VM**: the only place Starfield/Creation Kit/xEdit/MO2 run. Pulls this repo via git, builds, tests, pushes back.
- **Bridge**: this repo only. No shared network drive between the VMs — forces everything through commits/releases.

## Game side (Papyrus) — thin by design

Papyrus's job is reduced to three things, given known persistence fragility across Starfield updates (community guidance favors stateless scripts; a "Free Lanes" update broke Alias/ReferenceAlias/RefCollectionAlias calls in some mods):

1. Write race events (checkpoint crossed, race start/finish) to a flat JSONL log via trigger volumes + a polling script.
2. Own the minimum durable state that must survive a save without the sim running: `race_state` (IDLE/RUNNING/FINISHED), later `current_tier` and `active_rivalry_driver_id`. Always versioned, always defensively read.
3. Phase 1 grants its own reward directly in Papyrus (no live sim round-trip yet). Superseded at Sim Go-Live.

## Sim side — forked FTB core, not a from-scratch build

`F:\dev\oracle-radio\ftb_core\ftb_game.py` is the author's own ~35k-line motorsport management simulation (Driver/Engineer/Mechanic/Strategist/Car/Manufacturer/Part/Contract/Sponsorship/RegulationChange/Penalty/RDProject/UpgradePackage/Track/LapData/RaceResult/Budget/League/JobBoard/FreeAgent, its own `SimEventBus`, `WorldBuilder.generate_world`, `FTBSimulation.tick_simulation`). Rather than reimplementing an equivalent career/team/sponsor/contract system, this repo vendors and re-themes it:

1. Fork `ftb_game.py` / `ftb_names.py` / `ftb_race_day.py` into `sim/ftb_core/`, stripped of the `plugins.ftb_game` oracle-radio namespace-package dependency.
2. Prove the fork runs standalone (Phase 0.5) before any Starfield-specific theming.
3. Re-theme the domain vocabulary in `sim/starfield_theme/`: manufacturers/parts/cars → Starfield ship/rover brands and components; tracks → the three-tier venue system; leagues/seasons → tone-tiered series (corporate/frontier/outlaw/manufacturer-prototype/courier/pirate); sponsorships → soft, non-hard-locked faction/corp affiliations; driver/staff names → Settled Systems flavor.
4. Layer NCM-derived patterns FTB doesn't have natively (regional "heat," multiplicative "hype" payout scoring) as new modules (`sim/heat.py`, `sim/hype.py`), not bolted into the fork.

The sim ingests JSONL event logs matching loom's existing scout-shim schema (`type/title/body/priority/ts/id/tags` — see `F:\dev\oracle-radio\loom\shim_generator.py`) for free future compatibility with loom's `antenna_bridge`, without depending on oracle-radio's code.

## Sim Go-Live (deliberate future milestone)

Until the author decides they're ready for live season tracking/commentary, `sim/` runs **only on the Creative VM**, against fixture or manually-copied logs — never live-tailing real gameplay on the Gaming VM. Go-Live means: install Python + `sim/` on Gaming, wire live JSONL tailing, switch Phase 1's Papyrus-native reward logic to reading a sim-computed reward package.

## Native Systems Track (parallel)

SFSE is pre-alpha; Cassiopeia Papyrus Extender (~430 functions/~60 events) is the current ceiling for pure-Papyrus ship hooks. Deep ship-to-ship AI for wheel-to-wheel racing is planned via a custom native SFSE plugin, not avoided — scoped by reading Cassiopeia's source and SFSE's plugin API directly, starting once Phase 2's initial ship time-trial is proven.

## Phased roadmap

See `DECISIONS.md` for why each phase is ordered this way. Summary:

- **Phase 0** — toolchain proof (JSONL write → fixture parse → GitHub Release → MO2 install), no forking yet.
- **Phase 0.5** — fork FTB core, strip oracle-radio coupling, prove it runs standalone.
- **Phase 1** — one local REV-8 championship, solo time-trial, on the re-themed fork.
- **Phase 2** — ship racing (time-trial first); Native Systems Track begins scoping wheel-to-wheel ship AI.
- **Phase 3** — heat, hype, rivalry as new modules alongside the fork.
- **Phase 4** — hybrid endurance events + travel-hook integration (re-verify grav-jump precedent first).
- **Phase 5** — commentary/narrative (loom's grammar vs. FTB2's conversation-seed pattern, TBD), tone-tiered series, third venue tier, Sim Go-Live if not already triggered.
