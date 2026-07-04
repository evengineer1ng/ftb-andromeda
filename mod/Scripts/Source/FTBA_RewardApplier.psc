Scriptname FTBA_RewardApplier Hidden

; DRAFT — not yet compiled/verified. Phase 1 reward logic is deliberately self-contained
; in Papyrus (no live sim round-trip yet — see docs/ARCHITECTURE.md's "Companion Go-Live"
; / "Sim Go-Live" milestone). Superseded once the sim is installed on Gaming VM and can
; compute a real reward package instead.

Int Property Phase1CreditsReward = 500 AutoReadOnly
GlobalVariable Property FTBA_CurrentTier Auto
; Simple placeholder tier-bump rule for v1 — not meant to survive Sim Go-Live.

Function GrantPhase1Reward() Global
    Game.GetPlayer().AddItem(Game.GetFormFromFile(0x0000000F, "Starfield.esm") as Form, Phase1CreditsReward, true)
    ; 0x0000000F is Credits' vanilla FormID convention from Fallout/Skyrim-lineage games —
    ; NOT verified for Starfield specifically. Confirm the real Credits FormID on Gaming VM
    ; before trusting this line; a wrong ID will silently no-op or add the wrong item.
EndFunction
