# Main Missions

## Mission standard

Every mission must define a stable ID, act, date, region, location, historical classification, prerequisites, ordered objectives, failure states, success state, characters, factions, resources, rewards, reputation effects, and deterministic tests.

## Initial mission sequence

### BC_MISSION_PROLOGUE_IRON_LIST

Classification: `FICTION` within `RECONSTRUCTION` context.

Purpose: introduce Ezra's work, Ashgrove's schedule, the family separation, Isaiah's record, the first evidence of the regional network, and the physical revenge list.

The mission must not reveal the Elias Vane twist. It should present a real anomaly: a changed date, altered route, or inconsistent mark in the record.

### BC_MISSION_PROLOGUE_BROKEN_WHEEL

Classification: `FICTION` within `RECONSTRUCTION` context.

Purpose: teach observation, sabotage, tools, and route timing. Ezra discovers that a wagon is being prepared for a transfer.

### BC_MISSION_ESCAPE_ASHGROVE

Classification: `FICTION` within historical context.

Purpose: execute the escape, establish the first pursuit state, and introduce Mara Bell or another contact without making Ezra's escape an individual miracle.

### BC_MISSION_HUNT_FIRST_REFUGE

Classification: `FICTION` within `RECONSTRUCTION` context.

Purpose: reach the Great Dismal Swamp refuge, learn resource and trust requirements, and establish the first safe-house state.

## The Ledger investigation chain

The Isaiah branch is optional. The regional campaign can continue if the player does not investigate it. The chain is built from incomplete fictional records rather than a single confession.

### BC_MISSION_LEDGER_ASHGROVE_ENTRY

Act: `ACT_III_RECKONING`.

Classification: `FICTION` within `RECONSTRUCTION` context.

Location: Ashgrove records room or a copied ledger held by the escape network.

Prerequisites: `BC_MISSION_HUNT_FIRST_REFUGE`; access to the Ashgrove record source.

Objectives:

1. Identify Isaiah's original transfer entry.
2. Compare the entry with Ezra's copied marks.
3. Preserve the page or create a reliable transcription.
4. Mark the first contradiction: the transfer date does not match the presumed death window.

Evidence granted: `BC_EVIDENCE_ASHGROVE_TRANSFER_ENTRY`.

Failure states: page destroyed; transcription incomplete; alert increased. The main campaign continues, but the Isaiah chain may require an alternative source.

Success state: the transfer entry is preserved or reliably reconstructed.

### BC_MISSION_LEDGER_MANIFEST_FRAGMENT

Act: `ACT_III_RECKONING`.

Classification: `FICTION` within `RECONSTRUCTION` context.

Location: coastal warehouse, river office, or vessel records.

Prerequisites: `BC_EVIDENCE_ASHGROVE_TRANSFER_ENTRY` or a route contact with sufficient trust.

Objectives:

1. Locate a transport record connected to the Southampton lot.
2. Match physical description and ironworking skill rather than relying only on a name.
3. Determine that the entry was removed before departure.
4. Escape or negotiate without exposing the safe-house route.

Evidence granted: `BC_EVIDENCE_COASTWISE_MANIFEST_FRAGMENT`.

Failure states: manifest destroyed; route contact exposed; patrol alert increased. The evidence may still be recovered through the trader's accounts, but the direct route is closed.

Success state: Ezra establishes that Isaiah was removed from the planned transport before it sailed.

### BC_MISSION_LEDGER_TRADER_SETTLEMENT

Act: `ACT_III_RECKONING`.

Classification: `FICTION` within `RECONSTRUCTION` context.

Location: New Orleans commercial district and trader warehouse.

Prerequisites: `BC_EVIDENCE_COASTWISE_MANIFEST_FRAGMENT` or a completed trader investigation route.

Objectives:

1. Enter the trader's accounting space through disguise, a worker contact, or stealth.
2. Recover the settlement page associated with the Southampton lot.
3. Compare expected payment with the amount actually received.
4. Establish that the transaction was interrupted rather than completed normally.

Evidence granted: `BC_EVIDENCE_TRADER_SETTLEMENT_PAGE`.

Failure states: settlement page destroyed; trader alert reaches the patrol network; a route or disguise is consumed. The mission can continue through a public exposure approach, but the evidence may be incomplete.

Success state: the player confirms that the trader lost or deferred payment for Isaiah's transfer.

### BC_MISSION_LEDGER_VANE_ORDER

Act: `ACT_III_RECKONING`.

Classification: `FICTION` within `RECONSTRUCTION` context.

Location: county courthouse or a protected legal archive.

Prerequisites: at least two Ledger evidence items, or a direct Vane relationship state.

Objectives:

1. Obtain the original and corrected versions of the county order.
2. Compare dates, signatures, seals, and transfer language.
3. Prove that Elias Vane retained or delayed the document before departure.
4. Record the unresolved question of why he intervened.

Evidence granted: `BC_EVIDENCE_VANE_CORRECTED_ORDER`.

Failure states: archive sealed; witness intimidated; one document lost. The player may still confront Vane, but cannot establish the complete document chain.

Success state: Ezra learns that Vane interrupted one transfer without proving that he intended to free Isaiah.

### BC_MISSION_LEDGER_PRIVATE_ROUTE_NOTE

Act: `ACT_III_RECKONING`.

Classification: `FICTION`.

Location: trader correspondence cache, warehouse office, or intermediary's private papers.

Prerequisites: `BC_EVIDENCE_TRADER_SETTLEMENT_PAGE` and either `BC_EVIDENCE_VANE_CORRECTED_ORDER` or a completed trader dossier.

Objectives:

1. Identify the private note connected to the Southampton lot.
2. Match its shorthand to Isaiah's transfer record.
3. Confirm that another buyer was intended after the original transfer was blocked.
4. Decide whether to preserve, publish, or use the note as leverage.

Evidence granted: `BC_EVIDENCE_PRIVATE_ROUTE_NOTE`.

Failure states: note burned; intermediary escapes; publication exposes a safe house. The player retains partial evidence but cannot reach confirmed survival through this route alone.

Success state: Ezra understands that Vane protected Isaiah from one route without ending his enslavement.

### BC_MISSION_LEDGER_IRONWORK_SIGNAL

Act: `ACT_III_RECKONING`.

Classification: `FICTION` within `RECONSTRUCTION` context.

Location: workshop, river repair station, or hidden refuge connected to Isaiah's independent network.

Prerequisites: complete transfer chain, or alternative evidence plus sufficient free Black community trust and a prepared route.

Objectives:

1. Identify the distinctive ironworking mark.
2. Compare it with Ezra's memory of Isaiah's work.
3. Follow the instruction without exposing the refuge.
4. Choose whether to approach Isaiah, protect the route, or continue the regional investigation.

Evidence granted: `BC_EVIDENCE_IRONWORK_SIGNATURE`.

Failure states: route exposed; Isaiah relocates; contact is missed. The regional campaign continues, but reunion becomes unavailable or requires a later recovery mission.

Success state: Isaiah's survival is confirmed. Reunion is available only if the player also has a prepared route, sufficient trust, and the necessary protection resources.

## Branch outcomes

- No reliable chain: Isaiah remains `BC_ISAIAH_STATE_UNKNOWN` or `BC_ISAIAH_STATE_PRESUMED_DEAD`.
- Partial chain: Isaiah becomes `BC_ISAIAH_STATE_EVIDENCE_FOUND`.
- Complete documentary chain: Isaiah becomes `BC_ISAIAH_STATE_CONFIRMED_ALIVE`.
- Complete chain plus successful contact: Isaiah becomes `BC_ISAIAH_STATE_REUNITED`.
- Search window closed: Isaiah becomes `BC_ISAIAH_STATE_LOST`.

## Principal target pattern

Each principal target has three investigation missions and one resolution mission. Approaches may include stealth elimination, public exposure or sabotage, and capture or leverage. Target identity, campaign dates, and regional victory remain deterministic.

## Deterministic tests

- The same evidence inventory and mission state always produce the same Isaiah state.
- Destroying a document removes only the paths that depend on it; it does not randomly select another path.
- A failed investigation changes alert, resources, evidence, or route state through explicit rules.
- The regional campaign remains playable regardless of Isaiah's state.
- The epilogue never reveals information unavailable to Ezra in that playthrough.