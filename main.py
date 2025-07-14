import json
import os
from fastapi import FastAPI, Query
from pydantic import BaseModel
from enum import Enum
from typing import Annotated
from dataset_manager import get_dataset_file

app = FastAPI(
    title="FastAPI Items API",
    description="API para gestionar items con diferentes categorías",
    version="1.0.0"
)

# Configuración del archivo de dataset
DATASET_FILE = get_dataset_file()

@app.get("/")
async def root():
    """
    Endpoint raíz de la API.
    """
    return {"message": "Welcome to FastAPI Items API", "version": "1.0.0"}

@app.get("/items/")
async def get_items(skip: int = 0, limit: int = 1000):
    """
    Endpoint para obtener todos los items del dataset.
    """
    try:
        items = []
        with open(DATASET_FILE, "r") as file:
            items = json.load(file)
        return items[skip: skip + limit]  
    except FileNotFoundError:
        return {"error": "Dataset not found."}
    

@app.get("/items/{item_id}")
async def get_item_by_id(item_id: int):
    """
    Endpoint para obtener un item específico por su ID.
    """
    try:
        with open(DATASET_FILE, "r") as file:
            items = json.load(file)
        if 0 <= item_id < len(items):
            return items[item_id -1]
        else:
            return {"error": "Item not found."}
    except FileNotFoundError:
        return {"error": "Dataset not found."}

@app.get("/items/search/")
async def search_items(q: Annotated[str | None, Query(max_length=5)] = None):
    """
    Endpoint para buscar items por una consulta específica.
    """
    try:
        with open(DATASET_FILE, "r") as file:
            items = json.load(file)
        results = [item for item in items if q.lower() in item['name'].lower()]
        return results
    except FileNotFoundError:
        return {"error": "Dataset not found."}
    

class Item(BaseModel):
    name: str
    description: str
    brand: str
    price: float
    rating: float | None = 0
    in_stock: bool

class Category(str, Enum):
    electronics = "Electronics"
    home = "Home"
    food = "Food"
    toys = "Toys"
    tools = "Tools"

@app.post("/items/{category}")
async def create_item(item : Item, category: Category):
    """
    Endpoint para crear un nuevo item en una categoría específica.
    """
    try:
        with open(DATASET_FILE, "r") as file:
            items = json.load(file)
        new_item = item.dict()
        new_item['category'] = category.value
        new_item['id'] = len(items) + 1  # Asignar un ID único basado en la longitud actual
        items.append(new_item)
        
        with open(DATASET_FILE, "w") as file:
            json.dump(items, file, indent=4)
        
        return {"message": "Item created successfully.", "item": new_item}
    except FileNotFoundError:
        return {"error": "Dataset not found."}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """
    Endpoint para actualizar un item existente por su ID.
    """
    try:
        with open(DATASET_FILE, "r") as file:
            items = json.load(file)
        if 0 <= item_id < len(items):
            items[item_id - 1] = item.dict()
            with open(DATASET_FILE, "w") as file:
                json.dump(items, file, indent=4)
            return {"message": "Item updated successfully.", "item": items[item_id - 1]}
        else:
            return {"error": "Item not found."}
    except FileNotFoundError:
        return {"error": "Dataset not found."}
