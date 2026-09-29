# Bloque 2 — Economía, recursos, reputación y rescates

Este bloque formaliza la economía determinista de la preimplementación. Los recursos son estados persistentes, los consumos están declarados en datos y los rescates tienen requisitos explícitos. Ningún rescate se representa como un objeto coleccionable: cada persona conserva identidad, estado y destino.

## Reglas

- Las cantidades son enteros no negativos.
- Todo consumo debe estar declarado por una operación.
- Una operación solo puede ejecutarse si sus requisitos están satisfechos.
- La reputación se registra por facción y se modifica mediante deltas auditables.
- Un rescate puede estar `available`, `prepared`, `in_transit`, `delivered` o `failed_requirements`.
- `delivered` requiere una ubicación segura y una facción o red receptora.
- Los resultados no dependen de azar oculto.

## Recursos

El catálogo inicial incluye suministros médicos, alimentos, moneda, documentos, combustible, capacidad de transporte y plazas seguras. Cada recurso declara unidad, mínimo, máximo opcional y si puede transferirse.

## Rescates

Cada requisito declara recursos, reputación mínima, transporte, ruta y capacidad. La persona rescatada se identifica mediante `person_id`; su estado de bienestar y destino se mantienen separados de los inventarios.

## Reputación

Los deltas de reputación tienen identificador, causa, magnitud y facción afectada. La aplicación debe ser idempotente mediante `operation_id`.

## Próxima integración

El Bloque 3 puede conectar estos catálogos con misiones y estados de viaje sin introducir tiradas aleatorias ni referencias implícitas.
