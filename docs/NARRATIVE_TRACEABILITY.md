# Trazabilidad narrativa

| Elemento | Fuente narrativa | Runtime | Verificación |
|---|---|---|---|
| Isaiah | `narrative_characters.json` | operaciones de misión | `test_narrative_bible.py` |
| Ashgrove | secuencia, evidencia y escena | rescate Ashgrove | pasos 2–7 |
| Ironwork | secuencia, evidencia y escena | rescate Ironwork | pasos 2–7 |
| Facciones | relaciones y stakes | reputación | `test_narrative_steps_2_3.py` |
| Decisiones | escenas y elecciones | ramas | `test_narrative_steps_4_5.py` |
| Integración | bindings narrativos | operaciones, auditoría y escenarios | `test_narrative_steps_6_7.py` |

Cada binding debe apuntar a IDs existentes. Los cambios narrativos requieren actualizar datos, tests y documentación de forma coordinada.
