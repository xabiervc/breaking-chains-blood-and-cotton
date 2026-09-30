# Breaking Chains: Blood and Cotton

Preimplementación determinista de un juego narrativo sobre redes de fuga, rescates y decisiones bajo presión, con perspectiva coral y comunitaria.

## Estado

Versión: `0.1.0-preimplementation`.

La preimplementación incluye diseño de primeros minutos y primera hora, arco de campaña, estados narrativos, accesibilidad medible, plataformas, presupuestos técnicos, guardado y migración, telemetría privada, localización, auditoría, escenarios, narrativa canónica y tests.

## Verificación local

```bash
conda env create -f environment.yml
conda activate test
python tools/validate_content.py
python schemas/validate_schemas.py
python -m unittest discover -s tests -v
```

## Gates

Los criterios de `docs/VERTICAL_SLICE_GATES.md` separan lo que está definido de lo que está demostrado. La documentación no sustituye implementación, playtesting, consulta histórica, auditoría de accesibilidad ni una ejecución CI verde.
