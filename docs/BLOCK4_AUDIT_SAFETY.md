# Bloque 4 — Auditoría, trazabilidad y guardas de seguridad

Cada operación sensible debe producir un evento auditable con `operation_id`, entradas, salidas y resultado. La misma operación no puede aplicarse dos veces: `operation_id` es la clave de idempotencia.

Las guardas comprueban referencias, esquemas, balances, reputación, capacidad, transiciones permitidas y ausencia de azar no declarado.

Los resultados válidos son `accepted`, `rejected`, `failed_requirements` y `duplicate`. Un fallo de requisitos no debe mutar inventarios, reputación ni estados de rescate.
