# Determinism Specification

## Fixed state

Dates, historical anchors, main mission order, named target identities, core map regions, safe houses, required routes, rescue identities, named-character survival rules, and the 340-person final campaign outcome are fixed.

## Seeded state

NPC schedules, patrol placement, market values, travel outcomes, weather state, and minor ambient behaviour use stable date and state inputs. Cosmetic variation is allowed only inside the same seeded state.

## Forbidden randomness

No random main objectives, named-character survival, historical dates, antagonist identity, final campaign outcome, rescue identity, required route, or persistent evidence requirement.

## Persistent state

Completed mission IDs, bounty, alert, reputation, discovered routes, safe houses, rescued people, evidence, documents, inventory, transport condition, workshop state, faction state, newspaper state, public rumours, and final regional outcome.

## Stable IDs

Use immutable IDs such as `BC_MISSION_*`, `BC_CHAR_*`, `BC_FACTION_*`, `BC_REGION_*`, `BC_LOCATION_*`, `BC_EVIDENCE_*`, `BC_ROUTE_*`, and `BC_RESCUE_*`.