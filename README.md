# FastAPI Items API

API REST para gestionar items con diferentes categorías.

## Características

- Obtener todos los items con paginación
- Buscar items por ID
- Buscar items por nombre
- Crear nuevos items por categoría
- Actualizar items existentes

## Endpoints

- `GET /` - Endpoint raíz
- `GET /items/` - Obtener todos los items
- `GET /items/{item_id}` - Obtener item por ID
- `GET /items/search/` - Buscar items por consulta
- `POST /items/{category}` - Crear nuevo item
- `PUT /items/{item_id}` - Actualizar item

## Tecnologías

- FastAPI
- Pydantic
- Python 3.11+

## Despliegue

Esta API está desplegada en Render.
