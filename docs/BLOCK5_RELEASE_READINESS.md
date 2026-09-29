# Bloque 5 — Preparación de ejecución

El Bloque 5 consolida la preimplementación y deja explícita la única verificación externa pendiente: una ejecución real de GitHub Actions.

El repositorio contiene validación global, tests transversales, catálogos deterministas, contratos de auditoría y guardas de seguridad. La implementación no debe considerarse ejecutada hasta que el workflow publique un resultado exitoso.

Comandos de referencia:

```bash
python tools/validate_content.py
python -m unittest discover -s tests -v
```

Un resultado `success` del workflow permite cerrar la preimplementación; cualquier fallo debe corregirse antes de comenzar la implementación del producto.
