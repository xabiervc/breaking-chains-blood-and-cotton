# Criterios de entrega

Una versión puede pasar de preimplementación a implementación solo si cumple todas estas condiciones:

- El validador global termina correctamente.
- La validación de esquemas y JSON termina correctamente.
- Todos los tests terminan correctamente.
- GitHub Actions informa `success` sobre el commit candidato.
- No hay referencias huérfanas.
- No hay campos de azar no declarados.
- Las personas siguen separadas de los recursos.
- Las operaciones sensibles tienen auditoría e idempotencia.
- El checklist de preimplementación está actualizado.

Si una condición falla, la versión permanece en estado `preimplementation`.
