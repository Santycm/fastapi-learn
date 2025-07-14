#!/bin/bash
# Script de inicialización para Render

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Checking if large dataset exists..."
if [ ! -f "dataset_50000.json" ]; then
    echo "Large dataset not found, generating..."
    python generate_dataset.py
else
    echo "Large dataset found, skipping generation"
fi

echo "Starting FastAPI application..."
uvicorn main:app --host 0.0.0.0 --port $PORT
