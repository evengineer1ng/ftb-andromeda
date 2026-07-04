# Event Schema (game → sim contract)

Versioned. Bump `SCHEMA_VERSION` in both `mod/Scripts/Source/FTBA_EventLog.psc` and the sim-side parser whenever this changes, so a mismatched deploy fails loudly instead of silently misparsing.

## Wire format

Written via [PapyrusIniManipulator](https://www.nexusmods.com/starfield/mods/10704)'s `PushStringToIni`, not raw JSONL (see `DECISIONS.md`, 2026-07-04 — vanilla Papyrus has no file I/O; this is the confirmed-real mechanism).

- File: one INI file per playthrough/session (path TBD — depends on PapyrusIniManipulator's actual sandboxing, confirm on Gaming VM in Phase 0).
- Section: `[events]`
- Key: `evt_NNNNNN` (zero-padded, from `FTBA_EventCounter` GlobalVariable, increment-then-write so keys never collide)
- Value: a JSON string, e.g. `{"type":"checkpoint_crossed","tick":14,"checkpoint_index":2,"schema_version":1}`

## Event types (Phase 0/1)

| type | fields | meaning |
|---|---|---|
| `debug_ping` | `schema_version` | Phase 0 toolchain proof only |
| `race_started` | `schema_version` | Player entered the race trigger/state |
| `checkpoint_crossed` | `checkpoint_index`, `schema_version` | Player came within `CheckpointRadius` of `Checkpoints[checkpoint_index]` |
| `race_finished` | `elapsed_ticks`, `schema_version` | Final checkpoint reached |

`SCHEMA_VERSION = 1` as of 2026-07-04.

## Reading it back (sim side, once built)

Python's `configparser` reads the INI file; each value in `[events]` is JSON-decoded independently. Order events by the numeric suffix on the key, not file order (INI files aren't guaranteed to preserve write order across all writers).
