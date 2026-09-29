# Breaking Chains: Blood and Cotton

Preimplementación determinista de un juego narrativo sobre redes de fuga, rescates y decisiones bajo presión.

## Estado

Versión: `0.1.0-preimplementation`.

La preimplementación incluye catálogos de mundo, viajes, economía, rescates, reputación, auditoría, guardas, escenarios end-to-end, esquemas JSON, validación global y tests.

## Ejecutar localmente

```bash
conda env create -f environment.yml
conda activate test
python tools/validate_content.py
python schemas/validate_schemas.py
python -m unittest discover -s tests -v
```

## Criterio de entrega

La preparación no se considera verificada al 100 % hasta que GitHub Actions termina con `success` para el commit candidato. La configuración está en `.github/workflows/python-package-conda.yml`.

Consulta `docs/TRACEABILITY_MATRIX.md`, `docs/IMPLEMENTATION_HANDOFF.md` y `docs/PREIMPLEMENTATION_FINAL_STATUS.md` para la trazabilidad y el siguiente paso.
