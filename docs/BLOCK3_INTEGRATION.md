# Bloque 3 — Integración de misiones, economía y viajes

Este bloque conecta las misiones de los Bloques 1 y 2 con rescates, recursos, reputación y estados de viaje.

## Principios

- Cada operación tiene identificador estable y resultado determinista.
- Los recursos y la reputación son requisitos explícitos.
- Las transiciones de rescate solo usan estados declarados.
- Una persona rescatada nunca se trata como recurso.
- La resolución final debe ser auditable mediante la operación y sus entradas.

## Flujo

1. Una misión habilita una operación de preparación.
2. La operación verifica recursos, reputación y estado de viaje.
3. El rescate pasa de `available` a `prepared` y luego a `in_transit`.
4. La ruta alcanza `arrived` y el rescate puede pasar a `delivered`.
5. Si faltan requisitos, el resultado es `failed_requirements`, sin azar oculto.
