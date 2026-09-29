# Bloque 7 — Invariantes y regresión

El Bloque 7 convierte las reglas críticas de los bloques anteriores en pruebas de regresión.

## Invariantes

- Los identificadores son únicos dentro de cada catálogo.
- Las cantidades de recursos son enteros positivos cuando aparecen en operaciones.
- La reputación inicial permanece dentro de sus límites.
- Las transiciones de viaje apuntan a estados existentes.
- Las operaciones sensibles tienen eventos de auditoría e idempotencia.
- Los catálogos deterministas no contienen campos `random` no declarados.
- Las personas rescatadas permanecen separadas de los recursos.

El workflow debe ejecutar estas pruebas junto con el resto de la suite. Ningún documento marca por sí mismo una ejecución CI como exitosa.
