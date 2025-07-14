#!/bin/bash
# Script de inicialización para Render

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Starting FastAPI application..."
# El dataset se generará automáticamente si es necesario
uvicorn main:app --host 0.0.0.0 --port $PORT
