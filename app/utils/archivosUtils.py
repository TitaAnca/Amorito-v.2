import json
import os

def cargar_datos(archivo):
    with open(archivo, 'r') as file:
        return json.load(file)

def guardar_datos(archivo, datos):
    """Guarda los datos en un archivo JSON."""
    with open(archivo, 'w') as file:
        json.dump(datos, file, indent=4)