# Breaking Chains: Blood and Cotton

Preimplementación determinista de un juego narrativo sistémico y coral sobre redes de ayuda, rescate, información y supervivencia bajo la economía colonial del algodón.

## Fuente de verdad

La fuente única de verdad es `docs/CANONICAL_PREPRODUCTION_SPEC.md`. Los documentos históricos y subordinados están catalogados en `docs/ARCHIVED_DOCUMENTS.md`.

## Estado

Versión: `0.1.0-preimplementation`.

La preimplementación incluye bucle de juego, campaña, estados narrativos, decisiones, consecuencias, accesibilidad medible, representación histórica, plataforma, presupuestos técnicos, guardado, privacidad, localización, alcance, trazabilidad y gates de vertical slice.

## Verificación

```bash
conda env create -f environment.yml
conda activate test
python tools/validate_content.py
python schemas/validate_schemas.py
python -m unittest discover -s tests -v
```

La documentación no sustituye evidencia. CI verde, playtesting, consulta histórica, revisión cultural, auditoría de accesibilidad y métricas del vertical slice siguen siendo requisitos externos antes de producción.
