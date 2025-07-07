# Proyecto Hola Mundo con FastAPI

Este es un ejemplo básico de una aplicación web usando FastAPI en Python.

## Requisitos

- Python 3.7+
- FastAPI
- Uvicorn

## Instalación

Instala las dependencias con pip:

```bash
pip install fastapi uvicorn
```

## Uso

1. Ejecutar el script Python directamente:

```bash
python easy-api.py
```

# ó

2. Ejecuta el servidor con uvicorn:

```bash
uvicorn easy-api:app --reload
```

3. Abre en el navegador:

```
http://127.0.0.1:8000/hola_mundo
```

Deberías ver la respuesta:

```json
{"message": "Hola Mundo"}
```

## Notas

- El flag `--reload` permite que el servidor se reinicie automáticamente al detectar cambios en el código.
- Asegúrate de ejecutar el comando desde el directorio donde está el archivo `easy-api.py`.
