# Checklist de preimplementación

## Catálogos

- [x] Misiones, evidencias, regiones y localizaciones.
- [x] Personajes, facciones, rutas y transportes.
- [x] Estados de viaje deterministas.
- [x] Personas y requisitos de rescate.
- [x] Recursos, operaciones y reputación.
- [x] Operaciones de misión y transiciones de rescate.
- [x] Eventos de auditoría y guardas de seguridad.
- [x] Escenarios end-to-end de éxito y fallo.

## Integración

- [x] Referencias cruzadas entre bloques.
- [x] Estados de viaje conectados con rescates.
- [x] Economía separada de las personas rescatadas.
- [x] Idempotencia documentada.
- [x] Ausencia de azar oculto documentada.
- [x] Contratos verificados mediante escenarios completos.

## Verificación

- [x] Tests unitarios, transversales, invariantes y end-to-end presentes.
- [x] Validador global presente.
- [x] Validador de esquemas y JSON presente.
- [x] Workflow de GitHub Actions configurado.
- [ ] Ejecución CI confirmada en GitHub Actions.

La última casilla requiere una ejecución real del workflow; no debe marcarse manualmente.
