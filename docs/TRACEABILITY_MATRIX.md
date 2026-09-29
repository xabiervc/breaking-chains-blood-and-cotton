# Matriz final de trazabilidad

| Requisito | Datos | Validación | Tests | CI |
|---|---|---|---|---|
| Mundo narrativo | `data/missions.json`, `data/evidence.json`, `data/regions.json`, `data/locations.json` | `tools/validate_content.py` | contenido y rutas | workflow Conda |
| Viajes deterministas | `data/routes.json`, `data/transport.json`, `data/travel_states.json` | referencias y transiciones | `test_routes.py`, `test_travel_state.py`, invariantes | workflow Conda |
| Economía | `data/resources.json`, `data/reputation_factions.json` | recursos y operaciones | `test_economy_and_rescue.py` | workflow Conda |
| Rescates | `data/persons.json`, `data/rescue_requirements.json`, `data/rescue_transitions.json` | personas, destinos y estados | referencias cruzadas y end-to-end | workflow Conda |
| Integración | `data/mission_operations.json`, `data/scenarios.json` | operaciones y estados | Bloques 3, 7 y 9 | workflow Conda |
| Seguridad | `data/audit_events.json`, `data/safety_gates.json` | auditoría e idempotencia | Bloque 4 y pruebas transversales | workflow Conda |
| Contratos | `schemas/*.schema.json` | `schemas/validate_schemas.py` | `test_block8_ci_hardening.py` | workflow Conda |
