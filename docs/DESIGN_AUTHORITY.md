# Autoridad de diseño

## Fuente normativa

`docs/CANONICAL_PREPRODUCTION_SPEC.md` es la autoridad para identidad, bucle, campaña, perspectiva y alcance.

Las decisiones técnicas y de aceptación se rigen, respectivamente, por `docs/TECHNICAL_READINESS.md`, `docs/ACCESSIBILITY_ACCEPTANCE.md`, `docs/VERTICAL_SLICE_SPEC.md` y `docs/LEVEL_A_PREPRODUCTION_STANDARD.md`.

## Jerarquía

1. Fuente canónica y decisiones aprobadas.
2. Especificaciones especializadas.
3. Catálogos de datos y esquemas.
4. Tests y herramientas.
5. Documentos históricos o informativos.

Si dos documentos discrepan, prevalece el de mayor nivel y se registra una decisión en `docs/IMPLEMENTATION_DECISION_LOG.md` antes de modificar código o datos.

## Gobernanza

Cada cambio debe indicar alcance, motivo, impacto, evidencia requerida y responsable. La versión base para iniciar implementación controlada es el commit que el equipo congele después de revisar los gates.

Las hipótesis de prototipo no se presentan como decisiones cerradas. Las validaciones externas no se marcan como realizadas sin evidencia fechada.
