# Preparación técnica

## Plataformas objetivo

PC como plataforma primaria; mando y teclado como entradas soportadas. La matriz reserva una fase posterior para Steam Deck y consolas tras validar rendimiento y accesibilidad.

## Rendimiento y memoria

Objetivos de vertical slice: 60 FPS objetivo y mínimo de 30 FPS sostenidos en configuración mínima; tiempo de carga inicial menor de 8 segundos; memoria máxima documentada por plataforma en `data/technical_budgets.json`.

## Guardado y migración

Partidas versionadas, con migrador explícito por versión, copia de seguridad previa y rechazo seguro de datos incompatibles. Nunca sobrescribir una partida válida con una migración fallida.

## Telemetría

Opt-in, minimizada, sin contenido narrativo crudo ni identificadores personales. Se puede desactivar y borrar. Los eventos sirven para detectar bloqueos, accesibilidad y rendimiento, no para perfilar personas.

## Localización

Separar texto de lógica, usar IDs estables, soportar expansión de texto, pluralización y revisión cultural. Ninguna cadena narrativa se concatena de forma que impida traducción.

## Pruebas

Regresión automática, carga de catálogos, migración de guardados, errores recuperables, accesibilidad de interfaz y rendimiento del vertical slice.
