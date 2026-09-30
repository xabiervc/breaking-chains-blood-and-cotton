# Breaking Chains: Blood and Cotton

Preimplementación determinista de un juego narrativo sobre redes de fuga, rescates y decisiones bajo presión, con perspectiva coral y comunitaria.

## Estado

Versión: `0.1.0-preimplementation`.

La preimplementación incluye catálogos de mundo, viajes, economía, algodón, rescates, reputación, auditoría, guardas, escenarios end-to-end, narrativa canónica, escenas, decisiones, accesibilidad y un marco histórico, ético y de representación.

## Salvaguardas de producción

La producción está bloqueada hasta completar el protocolo de consulta con historiadores, especialistas en estudios afroamericanos, consultores comunitarios, lectores sensibles y especialistas en accesibilidad.

## Ejecutar localmente

```bash
conda env create -f environment.yml
conda activate test
python tools/validate_content.py
python schemas/validate_schemas.py
python -m unittest discover -s tests -v
```

## Criterio de calidad

El estándar de diseño y accesibilidad está documentado en `docs/QUALITY_BAR.md`, `docs/DESIGN_PILLARS.md` y `docs/ACCESSIBILITY_SPEC.md`. La obra no debe presentarse como históricamente validada ni lista para producción hasta completar revisión externa, playtesting y CI verde.
