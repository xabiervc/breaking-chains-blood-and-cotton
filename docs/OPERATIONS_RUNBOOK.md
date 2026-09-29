# Runbook operativo

## Validación local

Desde la raíz del repositorio:

```bash
python tools/validate_content.py
python -m unittest discover -s tests -v
```

## Diagnóstico

- Si falla la carga: revisar JSON y rutas bajo `data/`.
- Si falla una referencia: conservar el identificador declarado y corregir el catálogo origen o destino.
- Si falla un requisito: no aplicar consumos, reputación ni transición de rescate.
- Si aparece una operación duplicada: devolver `duplicate` usando `operation_id`.

## Cambios de datos

Todo nuevo identificador debe seguir el patrón de su catálogo. Toda transición debe señalar origen, destino y requisitos. No se permite azar implícito.

## Entrega

La entrega solo puede declararse lista cuando el workflow de GitHub Actions termina con resultado `success` y el commit revisado coincide con el código entregado.
