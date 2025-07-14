#!/usr/bin/env python3
"""
Script para generar un dataset grande en el servidor de producción.
Este script se ejecutará automáticamente durante el despliegue.
"""

import json
import random
from faker import Faker

fake = Faker()

def generate_large_dataset(size=50000):
    """Genera un dataset grande con datos sintéticos."""
    
    categories = ["Electronics", "Home", "Food", "Toys", "Tools"]
    brands = ["Samsung", "Apple", "Dell", "HP", "Sony", "LG", "Philips", "Bosch", "Nike", "Adidas"]
    
    items = []
    
    for i in range(1, size + 1):
        item = {
            "id": i,
            "name": fake.catch_phrase(),
            "description": fake.text(max_nb_chars=100),
            "brand": random.choice(brands),
            "price": round(random.uniform(10, 2000), 2),
            "rating": round(random.uniform(1, 5), 1),
            "in_stock": random.choice([True, False]),
            "category": random.choice(categories)
        }
        items.append(item)
    
    return items

def main():
    """Función principal para generar el dataset."""
    print("Generating large dataset...")
    
    # Generar dataset de 50,000 items
    dataset = generate_large_dataset(50000)
    
    # Guardar en archivo
    with open("dataset_50000.json", "w") as f:
        json.dump(dataset, f, indent=2)
    
    print(f"Dataset generated successfully with {len(dataset)} items!")

if __name__ == "__main__":
    main()
