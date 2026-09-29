# Handoff a implementación

La preimplementación queda organizada para iniciar la implementación únicamente después de confirmar el pipeline.

## Entradas

- Catálogos JSON bajo `data/`.
- Esquemas bajo `schemas/`.
- Validador global bajo `tools/validate_content.py`.
- Validador de esquemas bajo `schemas/validate_schemas.py`.
- Suite de tests bajo `tests/`.

## Orden recomendado

1. Implementar cargadores de catálogos.
2. Implementar validación de contratos.
3. Implementar motor de requisitos y consumos.
4. Implementar máquina de estados de viaje y rescate.
5. Implementar auditoría e idempotencia.
6. Conectar misiones con operaciones.
7. Reproducir los escenarios end-to-end.

## Bloqueo de entrega

No pasar a implementación si el workflow no termina en `success` para el commit revisado.
