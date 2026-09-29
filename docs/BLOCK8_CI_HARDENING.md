# Bloque 8 — Endurecimiento de CI

El workflow ejecuta tres capas en orden:

1. Validación global de catálogos y referencias.
2. Validación de que los esquemas y datos son JSON legible y están presentes.
3. Suite completa de tests unitarios, transversales e invariantes.

Un fallo en cualquiera de las capas detiene el job. La existencia del workflow no equivale a una ejecución exitosa; el commit candidato debe tener un resultado `success` visible en GitHub Actions.
