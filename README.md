# Breaking Chains: Blood and Cotton

Preimplementación determinista de un juego narrativo sistémico y coral sobre redes de ayuda, rescate, información y supervivencia bajo la economía colonial del algodón.

## Estado A

La definición de preproducción alcanza nivel A: la identidad, el bucle, la campaña, los sistemas conceptuales, la accesibilidad, la ética, el alcance, la trazabilidad y los criterios de aceptación están documentados. La autoridad documental está en `docs/DESIGN_AUTHORITY.md` y `docs/CANONICAL_PREPRODUCTION_SPEC.md`.

## Listo para iniciar

Puede comenzar un prototipo o vertical slice controlado. Las hipótesis están en `docs/PROTOTYPE_HYPOTHESES.md` y los gates operativos en `docs/VERTICAL_SLICE_SPEC.md` y `docs/VERTICAL_SLICE_EVIDENCE_TEMPLATE.md`.

## No afirmar todavía

No se debe afirmar que el control es divertido, que la representación está validada, que la accesibilidad funciona para usuarios reales, que el rendimiento cumple o que la producción plena está autorizada hasta obtener la evidencia correspondiente.

## Verificación local

```bash
conda env create -f environment.yml
conda activate test
python tools/validate_content.py
python schemas/validate_schemas.py
python -m unittest discover -s tests -v
```
