# Vector Circuit

A Starfield racing mod, in the lineage of Night City Motorsports (Cyberpunk 2077) and drawing on [loom](https://github.com/evengineer1ng)/oracle-radio's simulation and broadcast work.

## Toolchain

- **Creative VM** (this repo's home): source of truth for all mod source — Papyrus scripts, xEdit-edited plugins, docs, build scripts. No local Starfield install by design; game files never live here.
- **Gaming VM**: the only place Starfield, Creation Kit, and xEdit actually run. Pulls this repo to author/test against live game data, pushes changes back.
- **Bridge**: this GitHub repo. No direct VM-to-VM sharing — everything routes through commits/releases, on purpose, to force versioning discipline.
- **Distribution to Gaming VM's Mod Organizer 2**: build artifacts attached to GitHub Releases (tagged for milestones, a rolling pre-release for day-to-day iteration).

## Status

Pre-concept. No mod content yet — toolchain and concept design in progress.
