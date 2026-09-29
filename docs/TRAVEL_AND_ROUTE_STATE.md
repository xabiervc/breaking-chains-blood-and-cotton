# Travel and Route State

## Purpose

Travel is a deterministic simulation layer. It consumes time and resources, responds to weather and alert state, and persists route discovery and transport condition. It must never decide named-character survival or main narrative outcomes randomly.

## Persistent travel state

Each save stores:

- `current_region_id`
- `current_location_id`
- `discovered_route_ids`
- `blocked_route_ids`
- `route_alert_levels`
- `transport_state`
- `travel_clock`
- `weather_state`
- `evidence_profile`
- `safe_house_access`
- `community_trust`

## Deterministic inputs

A travel result is a pure function of:

```text
route_id
travel_start_date
weather_state
alert_level
transport_id
transport_condition
cargo_and_passenger_load
available_resources
evidence_profile
community_trust
```

The same inputs and save state must produce the same result.

## Resolution order

1. Verify that the route exists and has been discovered.
2. Verify that the route is not blocked.
3. Verify transport type and minimum condition.
4. Verify destination capacity and required access.
5. Calculate duration from base time and transport/weather modifiers.
6. Calculate food, water, medicine, and money costs.
7. Apply alert exposure and route-state changes.
8. Advance the travel clock.
9. Persist the resulting location, resources, alert, transport condition, and route state.

## Formula

The implementation may use:

```text
travel_hours = base_travel_hours / speed_modifier
travel_hours *= weather_modifier
travel_hours *= alert_delay_modifier
resource_cost = base_route_cost * transport_resource_modifier * load_modifier
alert_change = route_alert_modifier + evidence_exposure_modifier + weather_visibility_modifier
```

Modifiers must be data-driven and deterministic. No random roll is allowed for required routes or mission-critical travel.

## Failure states

- `ROUTE_NOT_DISCOVERED`
- `ROUTE_BLOCKED`
- `TRANSPORT_UNAVAILABLE`
- `TRANSPORT_CONDITION_TOO_LOW`
- `INSUFFICIENT_RESOURCES`
- `CAPACITY_EXCEEDED`
- `ACCESS_REQUIREMENT_MISSING`
- `DETERMINISTIC_TRAVEL_DELAY`

A travel delay changes time, resource consumption, and alert state through explicit rules. It does not randomly kill named characters or delete rescue identities.

## Weather states

Weather is date-seeded and region-specific. Cosmetic variation may occur inside a weather state, but the gameplay modifier is fixed for the relevant travel input.

## Route discovery

A route becomes discovered through a mission, trusted contact, scouting activity, or recovered document. Discovery is persistent. If a route is later blocked, its discovery remains known but its current state changes to blocked.

## Isaiah branch

The Isaiah investigation may add or remove route access, evidence shortcuts, and contact requirements. It must never reveal information unavailable to Ezra in that playthrough.

## Validation requirements

Validate route IDs, transport IDs, region and location references, resource names, alert levels, numeric modifiers, valid state transitions, and required deterministic inputs.