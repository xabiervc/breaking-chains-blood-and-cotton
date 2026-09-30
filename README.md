# Breaking Chains: Blood and Cotton

Preimplementación determinista de un juego narrativo sistémico y coral sobre redes de ayuda, rescate, información y supervivencia bajo la economía colonial del algodón.

## Estado

`0.1.0-preimplementation — frozen_for_prototype`.

La definición documental alcanza nivel A y está congelada para iniciar un prototipo o vertical slice controlado. La autoridad está en `docs/DOCUMENT_AUTHORITY_INDEX.md` y `docs/DESIGN_AUTHORITY.md`.

## Siguiente fase

Construir el vertical slice descrito en `docs/VERTICAL_SLICE_SPEC.md` y registrar cada resultado en `docs/VERTICAL_SLICE_EVIDENCE_TEMPLATE.md` y `docs/OPEN_VALIDATION_REGISTER.md`.

## Condición de producción

No se autoriza producción completa hasta que CI, vertical slice, playtesting, consulta histórica/cultural, lectores sensibles, auditoría de accesibilidad, rendimiento y localización piloto tengan evidencia fechada y revisada.

## Verificación local

```bash
conda env create -f environment.yml
conda activate test
python tools/validate_content.py
python schemas/validate_schemas.py
python -m unittest discover -s tests -v
```
