# Endings and Failure States

## Two axes

The final state uses two independent axes:

1. Regional campaign outcome.
2. Isaiah and Ezra's personal outcome.

The player can win or lose the regional campaign while either discovering or failing to discover the truth about Isaiah.

## Regional outcomes

- `BC_END_REGIONAL_VICTORY`: the Ashgrove-linked network is dismantled and the canonical full-campaign liberation total reaches 340.
- `BC_END_REGIONAL_PARTIAL`: the network is damaged but survives in another form; the full liberation total is not reached.
- `BC_END_REGIONAL_DEFEAT`: the network survives, the resistance is fragmented, and the campaign's regional objective fails.

The national historical context remains unchanged in every outcome. Slavery continues nationally beyond the campaign period.

## Personal outcomes

- `BC_END_PERSONAL_REUNITED`: Ezra and Isaiah meet and establish a conditional relationship.
- `BC_END_PERSONAL_CONFIRMED_SEPARATED`: Isaiah is confirmed alive but no reunion occurs.
- `BC_END_PERSONAL_UNRESOLVED`: Ezra never obtains reliable confirmation.
- `BC_END_PERSONAL_LOST`: the available search route closes and no further evidence can be recovered.

## Endings must not be simple morality scores

A regional victory can be violent, costly, evidence-driven, refuge-driven, or coordinated. A regional defeat can still contain acts of courage, rescued individuals, preserved testimony, or surviving relationships.

## Victory variants

- `BC_VICTORY_NETWORK`: evacuation and safe-house capacity are the dominant achievement.
- `BC_VICTORY_RECORDS`: evidence, printing, and public exposure are the dominant achievement.
- `BC_VICTORY_RUPTURE`: sabotage and infrastructure destruction are the dominant achievement.

These variants alter costs, reputations, surviving infrastructure, and epilogue emphasis without changing the national timeline.

## Failure design

Failure is persistent rather than a reload-only event. Failed operations can close routes, destroy evidence, increase patrol activity, reduce trust, separate people, and change resource requirements.

Main failure must remain deterministic. Given identical state, dates, inputs, and decisions, the same outcome must occur.

## Epilogue principles

Do not secretly confirm Isaiah's survival if the player never discovered it. Do not erase losses because the regional campaign was successful. Do not make a white ally the narrator of the victory. The final voice should prioritize the communities and people who carried the resistance.