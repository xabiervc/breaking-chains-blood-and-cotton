# Matriz de decisiones y consecuencias

| Decisión | Variable | Escena | Resultado inmediato | Consecuencia persistente |
|---|---|---|---|---|
| Compartir entrada de Ashgrove | `information_exposure` | `BC_SCENE_ASHGROVE_PREPARATION` | ayuda más rápida | aumenta vigilancia y confianza potencial |
| Proteger la entrada | `information_protection` | `BC_SCENE_ASHGROVE_PREPARATION` | ayuda más lenta | reduce exposición y estrecha la ventana |
| Verificar señal de Ironwork | `ironwork_signal_verified` | `BC_SCENE_IRONWORK_SIGNAL` | desbloquea rescate | aumenta confianza abolicionista |
| Retrasar la salida | `rescue_window_narrows` | `BC_SCENE_IRONWORK_SIGNAL` | red más segura | capacidad de rescate más limitada |
| Entregar Ashgrove | `rescue_delivered` | escena de destino seguro | personas llegan a refugio | capacidad y reputación cambian |
| Fallar requisitos | `failed_requirements` | escena de recuperación | no hay mutación parcial | se abre recuperación o nueva preparación |

Cada fila debe tener implementación, test y evento de auditoría antes de producción.
