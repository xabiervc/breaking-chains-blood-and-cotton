# Bloque 9 — Verificación end-to-end

Este bloque reúne los contratos de los bloques anteriores en escenarios completos.

## Escenario aceptado

La operación de Ashgrove parte de `available`, atraviesa `in_transit`, alcanza `arrived` y termina en `delivered`.

## Escenario rechazado

La operación de Ironwork termina en `failed_requirements` cuando no se cumplen los requisitos. No se entrega el rescate ni se aplican mutaciones parciales.

Ambos escenarios son deterministas, referencian identificadores existentes y sirven como base para la futura implementación del motor.
