import json
import os
from pathlib import Path

def ensure_dataset_exists():
    """
    Asegura que existe un dataset para la aplicación.
    Si no existe dataset_50000.json, usa sample_dataset.json como fallback.
    """
    large_dataset = "dataset_50000.json"
    sample_dataset = "sample_dataset.json"
    
    if os.path.exists(large_dataset):
        return large_dataset
    elif os.path.exists(sample_dataset):
        print(f"Warning: {large_dataset} not found, using {sample_dataset}")
        return sample_dataset
    else:
        # Crear un dataset mínimo si no existe ninguno
        minimal_dataset = [
            {
                "id": 1,
                "name": "Sample Item",
                "description": "This is a sample item",
                "brand": "Sample Brand",
                "price": 99.99,
                "rating": 4.0,
                "in_stock": True,
                "category": "Electronics"
            }
        ]
        
        with open(sample_dataset, "w") as f:
            json.dump(minimal_dataset, f, indent=4)
        
        print(f"Created minimal dataset: {sample_dataset}")
        return sample_dataset

def get_dataset_file():
    """
    Retorna el archivo de dataset a usar, priorizando variables de entorno.
    """
    # Prioridad: variable de entorno > dataset grande > dataset de ejemplo
    env_dataset = os.getenv("DATASET_FILE")
    if env_dataset and os.path.exists(env_dataset):
        return env_dataset
    
    return ensure_dataset_exists()
