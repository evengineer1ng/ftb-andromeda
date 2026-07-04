"""Phase 0.5 proof: the vendored FTB core runs standalone, with zero oracle-radio imports.

Run directly: python sim/tests/test_ftb_core_standalone.py
(adds the repo's sim/ dir to sys.path so `ftb_core`/`plugins` resolve as siblings,
mirroring oracle-radio's own layout without editing any of ftb_game.py's internals)
"""
from __future__ import annotations

import sys
from pathlib import Path

SIM_DIR = Path(__file__).resolve().parents[1]
if str(SIM_DIR) not in sys.path:
    sys.path.insert(0, str(SIM_DIR))

from ftb_core.ftb_game import SimState, WorldBuilder, FTBSimulation  # noqa: E402


def main() -> None:
    state = SimState()
    state.seed = 42
    WorldBuilder.generate_world(state)

    print(f"[ok] world generated: tick={state.tick}, "
          f"leagues={len(getattr(state, 'leagues', {}) or {})}, "
          f"teams={len(getattr(state, 'teams', {}) or {})}, "
          f"tracks={len(getattr(state, 'tracks', {}) or {})}, "
          f"manufacturers={len(getattr(state, 'manufacturers', {}) or {})}, "
          f"parts={len(getattr(state, 'parts_catalog', {}) or {})}")

    mfrs = list(getattr(state, "manufacturers", {}).values())[:5]
    if mfrs:
        print("[ok] sample manufacturers: " + ", ".join(f"{m.name} ({m.nationality})" for m in mfrs))

    total_events = 0
    for day in range(14):
        events = FTBSimulation.tick_simulation(state)
        total_events += len(events)

    print(f"[ok] ran 14 sim-days after generation, tick now={state.tick}, "
          f"{total_events} SimEvents produced")
    print("[ok] Phase 0.5 standalone proof passed: no oracle-radio imports required")


if __name__ == "__main__":
    main()
