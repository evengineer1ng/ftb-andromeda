Scriptname FTBA_EventLog Hidden

; DRAFT — not yet compiled/verified (Creative VM has no Starfield/Papyrus compiler by design;
; see docs/DECISIONS.md 2026-07-04). Compile and fix on Gaming VM via the standalone Papyrus
; compiler. Stateless global-function script by design (see docs/ARCHITECTURE.md's "thin by
; design" section) — no persistent script state here, only the counter GlobalVariable does.
;
; Depends on PapyrusIniManipulator (github.com/BellCubeDev/papyrus-index data/Starfield/ini-manipulator,
; nexusmods.com/starfield/mods/10704) for PushStringToIni. Confirm its actual write-path
; sandboxing on Gaming VM before relying on a specific IniPath value below.

Int Property SchemaVersion = 1 AutoReadOnly

; TBD once PapyrusIniManipulator's path sandboxing is confirmed on Gaming VM — see EVENT_SCHEMA.md.
String Property IniPath = "FTBA_Events.ini" AutoReadOnly

GlobalVariable Property FTBA_EventCounter Auto
; Must be created as a new GlobalVariable form in xEdit and wired to this property.

Function LogEvent(String eventType, String extraJsonFields = "") Global
    ; extraJsonFields: pre-formatted JSON fragment WITHOUT surrounding braces, e.g. "\"checkpoint_index\":2,"
    ; (kept as plain string concatenation rather than a real JSON encoder — Papyrus has no
    ; native JSON writer either; if this gets unwieldy, revisit before Phase 3)
    Int counter = FTBA_EventCounter.GetValueInt() + 1
    FTBA_EventCounter.SetValueInt(counter)

    String key = "evt_" + PadCounter(counter)
    String value = "{\"type\":\"" + eventType + "\"," + extraJsonFields + "\"schema_version\":" + SchemaVersion + "}"

    PapyrusIniManipulator.PushStringToIni(IniPath, "events", key, value, true)
EndFunction

String Function PadCounter(Int counter) Global
    ; Papyrus has no zero-pad builtin; simple manual padding to 6 digits.
    ; Assumes StringUtil.GetLength exists in Starfield (carried over from Skyrim/FO4's
    ; native StringUtil script) — not independently verified, check on Gaming VM.
    String s = counter as String
    While StringUtil.GetLength(s) < 6
        s = "0" + s
    EndWhile
    Return s
EndFunction
