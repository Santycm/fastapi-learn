import json
import os
from pathlib import Path

def generate_large_dataset():
    """Genera el dataset extenso usando la función de generate_dataset.py"""
    try:
        from generate_dataset import generate_large_dataset as gen_dataset
        print("Generating large dataset (50,000 items)...")
        dataset = gen_dataset(50000)
        
        with open("dataset_50000.json", "w") as f:
            json.dump(dataset, f, indent=2)
        
        print("Large dataset generated successfully!")
        return "dataset_50000.json"
    except ImportError:
        print("Warning: Could not import generate_dataset module")
        return None
    except Exception as e:
        print(f"Error generating large dataset: {e}")
        return None

def ensure_dataset_exists():
    """
    Asegura que existe un dataset para la aplicación.
    Si no existe dataset_50000.json, lo genera automáticamente.
    """
    large_dataset = "dataset_50000.json"
    sample_dataset = "sample_dataset.json"
    
    if os.path.exists(large_dataset):
        return large_dataset
    
    # Intentar generar el dataset extenso
    print(f"{large_dataset} not found, generating it...")
    generated = generate_large_dataset()
    if generated and os.path.exists(generated):
        return generated
    
    # Fallback: usar o crear dataset de ejemplo
    if os.path.exists(sample_dataset):
        print(f"Warning: Could not generate {large_dataset}, using {sample_dataset}")
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
