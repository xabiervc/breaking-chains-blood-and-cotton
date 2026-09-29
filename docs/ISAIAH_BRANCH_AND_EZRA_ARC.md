# Isaiah Branch and Ezra Arc

## Purpose

Isaiah Coffin is a major optional personal storyline. The regional campaign can continue if Ezra never discovers the truth, but the discovery and reunion materially affect Ezra's personal development, relationships, leadership style, and some campaign costs.

## Canon

Isaiah was sold before the game begins and was later removed from a transfer toward New Orleans. Elias Vane altered or delayed the document that would have completed that transfer. Vane did not free Isaiah and remained complicit in other sales. Isaiah survived and developed an independent information and escape network.

This truth is not automatically revealed. A player may complete the game with Isaiah presumed dead, with evidence but no certainty, with confirmed survival but no reunion, or with a reunion.

## Isaiah states

- `BC_ISAIAH_STATE_UNKNOWN`: Ezra has no reliable evidence beyond the original disappearance.
- `BC_ISAIAH_STATE_PRESUMED_DEAD`: Ezra accepts the most likely explanation as death.
- `BC_ISAIAH_STATE_EVIDENCE_FOUND`: conflicting records show that the original death assumption is unreliable.
- `BC_ISAIAH_STATE_CONFIRMED_ALIVE`: evidence identifies Isaiah as alive, but contact has not occurred.
- `BC_ISAIAH_STATE_REUNITED`: Ezra and Isaiah have met.
- `BC_ISAIAH_STATE_LOST`: the search window closes without a reliable resolution.

## Evidence chain

The Ledger can connect the following fictional evidence items:

- `BC_EVIDENCE_ASHGROVE_TRANSFER_ENTRY`: original Ashgrove transfer entry.
- `BC_EVIDENCE_COASTWISE_MANIFEST_FRAGMENT`: transport record fragment with a matching physical description.
- `BC_EVIDENCE_TRADER_SETTLEMENT_PAGE`: incomplete commercial account showing an interrupted transaction.
- `BC_EVIDENCE_VANE_CORRECTED_ORDER`: two versions of a county order with a delayed or altered transfer.
- `BC_EVIDENCE_PRIVATE_ROUTE_NOTE`: fictional note indicating that Isaiah was removed from the Southampton lot.
- `BC_EVIDENCE_IRONWORK_SIGNATURE`: a technical mark that identifies Isaiah's independent network.

The chain proves that Isaiah was removed from one transfer. It does not automatically prove where he is now or why Vane acted.

## Discovery rules

The discovery path is optional and deterministic. It depends on evidence collected, access to Vane's records, search priority, dates, route state, and whether the player preserves or destroys relevant documents.

Suggested thresholds:

- `0–1` relevant evidence items: `UNKNOWN` or `PRESUMED_DEAD`.
- `2–3` relevant items: `EVIDENCE_FOUND`.
- Complete transfer and route chain: `CONFIRMED_ALIVE`.
- Confirmed survival plus a prepared route and sufficient community trust: `REUNITED`.

A failure to investigate can close the search window. The game should not show a secret confirmation after the window closes.

## Ezra personal states

Track separately from Isaiah's factual state:

- `BC_EZRA_ARC_ISOLATED`: grief and distrust dominate.
- `BC_EZRA_ARC_FIXATED`: revenge controls decisions.
- `BC_EZRA_ARC_QUESTIONING`: Ezra begins to question his assumptions.
- `BC_EZRA_ARC_CONNECTED`: Ezra respects other people's agency and accepts shared leadership.
- `BC_EZRA_ARC_COLLECTIVE_LEADER`: Ezra leads through coordination rather than personal control.

Discovering Isaiah does not automatically advance Ezra's arc. A reunion followed by controlling or reckless behaviour can leave Ezra `FIXATED` or `QUESTIONING`.

## Mara and Ruth effects

Mara evaluates Ezra's effect on the safety and autonomy of the network. Ruth evaluates whether Ezra can care without controlling.

- Respecting Isaiah's decisions increases Mara trust and Ruth trust.
- Using the network solely to recover Isaiah reduces trust.
- Delaying a revenge action to protect a refuge increases trust.
- Treating Isaiah as a mission objective reduces Isaiah cooperation and may close refuge access.

## End-state combinations

The regional campaign is independent of the personal branch:

- Regional victory + Isaiah reunited: collective victory with partial personal reconciliation.
- Regional victory + Isaiah confirmed but not reunited: the network wins while the family remains separated.
- Regional victory + Isaiah presumed dead: Ezra builds a legacy from unresolved grief.
- Regional defeat + Isaiah reunited: the brothers survive or cooperate, but the system remains strong.
- Regional defeat + Isaiah not discovered: both the regional network and Ezra's personal search fail.

## Narrative rules

Do not make Isaiah a collectible, reward, or passive rescue target. Do not reveal the truth outside Ezra's available evidence. Do not force one canonical emotional response. The unresolved route must remain meaningful and must not be labelled as a failed playthrough.

## Accessibility and content

Flag scenes involving family separation, presumed death, captivity, and reunion. Allow content warnings without removing the causal consequences of the branch.