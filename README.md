# Breaking Chains: Blood and Cotton

Preimplementación determinista de un juego narrativo sobre redes de fuga, rescates y decisiones bajo presión.

## Estado

Versión: `0.1.0-preimplementation`.

La preimplementación incluye catálogos de mundo, viajes, economía, rescates, reputación, auditoría, guardas, escenarios end-to-end, narrativa canónica, escenas, decisiones, accesibilidad, esquemas JSON, validación global y tests.

## Ejecutar localmente

```bash
conda env create -f environment.yml
conda activate test
python tools/validate_content.py
python schemas/validate_schemas.py
python -m unittest discover -s tests -v
```

## Criterio de calidad

`docs/QUALITY_BAR.md`, `docs/DESIGN_PILLARS.md` y `docs/ACCESSIBILITY_SPEC.md` convierten el objetivo de calidad en criterios verificables. Alcanzar un estándar de premios requiere además implementación, playtesting, revisión humana, localización y una ejecución CI verde.

Consulta `docs/TRACEABILITY_MATRIX.md`, `docs/IMPLEMENTATION_HANDOFF.md` y `docs/PREIMPLEMENTATION_FINAL_STATUS.md` para la trazabilidad y el siguiente paso.
