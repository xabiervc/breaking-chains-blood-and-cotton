# Checklist de preimplementación

## Catálogos

- [x] Misiones, evidencias, regiones y localizaciones.
- [x] Personajes, facciones, rutas y transportes.
- [x] Estados de viaje deterministas.
- [x] Personas y requisitos de rescate.
- [x] Recursos, operaciones y reputación.
- [x] Operaciones de misión y transiciones de rescate.
- [x] Eventos de auditoría y guardas de seguridad.

## Integración

- [x] Referencias cruzadas entre bloques.
- [x] Estados de viaje conectados con rescates.
- [x] Economía separada de las personas rescatadas.
- [x] Idempotencia documentada.
- [x] Ausencia de azar oculto documentada.

## Verificación

- [x] Tests unitarios y transversales presentes.
- [x] Validador global presente.
- [x] Workflow de GitHub Actions configurado.
- [ ] Ejecución CI confirmada en GitHub Actions.

La última casilla requiere una ejecución real del workflow; no debe marcarse manualmente.
