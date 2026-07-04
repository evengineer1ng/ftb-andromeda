Scriptname FTBA_RaceQuest Extends Quest

; DRAFT — not yet compiled/verified. Attach to a NEW Quest with NO new aliases (the
; xEdit new-alias bug — see docs/DECISIONS.md 2026-07-04 — makes duplicating a vanilla
; quest with existing aliases the safer path if aliases end up needed later; this v1
; deliberately needs none).
;
; Checkpoints are pre-existing vanilla references in the chosen location, wired via the
; Checkpoints[] property in xEdit/CK's property editor — NOT newly-placed objects
; (avoids needing Creation Kit's 3D viewport at all, see docs/ARCHITECTURE.md).

GlobalVariable Property FTBA_RaceState Auto
; 0 = Idle, 1 = Running, 2 = Finished. Versioned/defensive: always check State() before
; trusting this rather than assuming it's been initialized (Papyrus alias/global fragility
; risk — see docs/DECISIONS.md's risk register).

ObjectReference[] Property Checkpoints Auto
Float Property CheckpointRadius = 500.0 Auto
Float Property PollIntervalSeconds = 0.5 Auto

Int CurrentCheckpointIndex = 0

Function StartRace()
    If GetState() != 0
        Return ; already running or finished; ignore duplicate start
    EndIf
    FTBA_RaceState.SetValueInt(1)
    CurrentCheckpointIndex = 0
    FTBA_EventLog.LogEvent("race_started")
    RegisterForSingleUpdate(PollIntervalSeconds)
EndFunction

Event OnUpdate()
    If GetState() != 1
        Return ; not running; stop polling
    EndIf

    Actor player = Game.GetPlayer()
    ObjectReference target = Checkpoints[CurrentCheckpointIndex]

    If target != None && player.GetDistance(target) <= CheckpointRadius
        FTBA_EventLog.LogEvent("checkpoint_crossed", "\"checkpoint_index\":" + CurrentCheckpointIndex + ",")
        CurrentCheckpointIndex += 1

        If CurrentCheckpointIndex >= Checkpoints.Length
            FinishRace()
            Return
        EndIf
    EndIf

    RegisterForSingleUpdate(PollIntervalSeconds)
EndEvent

Function FinishRace()
    FTBA_RaceState.SetValueInt(2)
    FTBA_EventLog.LogEvent("race_finished")
    FTBA_RewardApplier.GrantPhase1Reward()
EndFunction

Int Function GetState()
    Return FTBA_RaceState.GetValueInt() as Int
EndFunction
