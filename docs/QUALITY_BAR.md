# Quality bar

Este repositorio usa un estándar aspiracional de nivel de premio, pero no declara haberlo alcanzado sin pruebas de producción.

## Diseño y jugabilidad

- El bucle debe ser legible: investigar, preparar, viajar, decidir y asumir consecuencias.
- Cada elección debe cambiar al menos uno de: información, recursos, reputación, riesgo o relación.
- Todo riesgo debe comunicar causa, coste y resultado posible antes de la decisión.
- No se usa azar oculto.
- Una ruta alternativa debe existir cuando el estado de una operación lo permita.

## Narrativa

- Los personajes tienen objetivos, límites, relaciones y agencia.
- Las evidencias desbloquean escenas o decisiones comprensibles.
- Las consecuencias deben ser visibles y coherentes con la elección.
- La representación de la esclavitud evita trivialización, coleccionismo o violencia ornamental.

## Accesibilidad

- Texto redimensionable y contraste suficiente.
- Subtítulos configurables y sin depender solo del audio.
- Remapeo de controles y alternativas a acciones de tiempo.
- Modos de asistencia sin bloquear contenido narrativo.
- Mensajes de error claros y reversibilidad cuando sea posible.

## Calidad técnica

- Validación de datos y esquemas en CI.
- Tests unitarios, integración, invariantes y escenarios.
- Errores deterministas y auditables.
- Dependencias fijadas mediante `environment.yml`.
- Ninguna afirmación de calidad final sin playtesting, revisión humana y CI verde.
