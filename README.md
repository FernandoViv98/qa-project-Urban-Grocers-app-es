# Proyecto Urban Grocers de Pruebas Automatizadas - Creación de Kits

# Proyecto de Pruebas Automatizadas - Creación de Kits

Este proyecto tiene como objetivo validar automáticamente el comportamiento del sistema al crear kits, realizando pruebas positivas y negativas sobre el parámetro `"name"` en el cuerpo de la solicitud. Las pruebas verifican cómo responde la API ante diferentes tipos de datos, longitudes y formatos para asegurar la calidad y robustez del servicio.

También se incluyen pruebas similares para el parámetro `firstName` al momento de crear un usuario/a, siguiendo criterios de validación equivalentes.

## Tecnologías utilizadas

- **Lenguaje:** Python
- **Entorno de desarrollo:** PyCharm
- **Librerías necesarias:** `pytest`, `requests`

## Casos de prueba incluidos (parámetro `name`)

Las pruebas automatizadas cubren los siguientes escenarios para la creación de kits:

| # | Escenario | Entrada (`kit_body`) | Código esperado |
|---|-----------|----------------------|-----------------|
| 1 | Mínimo permitido (1 carácter) | `{"name": "a"}` | 201 |
| 2 | Máximo permitido (511 caracteres) | `{"name": "..."}` | 201 |
| 3 | Cadena vacía (0 caracteres) | `{"name": ""}` | 400 |
| 4 | Supera el límite (512 caracteres) | `{"name": "..."}` | 400 |
| 5 | Caracteres especiales permitidos | `{"name": "№%@,"}` | 201 |
| 6 | Espacios permitidos | `{"name": " A Aaa "}` | 201 |
| 7 | Números permitidos | `{"name": "123"}` | 201 |
| 8 | Falta el campo `"name"` | `{}` | 400 |
| 9 | Tipo incorrecto (entero) | `{"name": 123}` | 400 |

## Requisitos previos

Asegúrate de tener instalado las librerias de pytest y requests:

## Para instalar pytest y requests ve a la pantalla de comando y coloca estos comandos (tambien se pueden instalar desde Python Packages desde su buscador)
- pip install pytest 
- pip install requests