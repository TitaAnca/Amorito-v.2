import os
import json

# Función para cargar datos de un archivo JSON
def cargar_datos_json(ruta_archivo):
    """Carga los datos de un archivo JSON."""
    if not os.path.exists(ruta_archivo):
        # Si el archivo no existe, devuelve un diccionario vacío
        return {}
    
    with open(ruta_archivo, 'r') as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            # Si ocurre un error al leer el archivo JSON, retorna un diccionario vacío
            return {}

# Función para guardar datos en un archivo JSON
def guardar_datos_json(ruta_archivo, datos):
    """Guarda los datos en un archivo JSON."""
    try:
        with open(ruta_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)
        return True
    except Exception as e:
        # Si ocurre un error al guardar los datos, imprime el error y retorna False
        print(f"Error al guardar el archivo {ruta_archivo}: {e}")
        return False

# Función para verificar si un archivo existe
def archivo_existe(ruta_archivo):
    """Verifica si un archivo existe en el sistema."""
    return os.path.exists(ruta_archivo)

# Función para validar la edad (por ejemplo, para el rango de edad en la app de citas)
def validar_edad(edad):
    """Valida si la edad proporcionada está dentro de un rango aceptable."""
    if not isinstance(edad, int):
        return False
    return 18 <= edad <= 80

# Función para obtener la edad a partir de la fecha de nacimiento (si es necesario)
from datetime import datetime

def calcular_edad(fecha_nacimiento):
    """Calcula la edad a partir de una fecha de nacimiento (formato 'YYYY-MM-DD')."""
    try:
        nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
        today = datetime.today()
        edad = today.year - nacimiento.year
        if today.month < nacimiento.month or (today.month == nacimiento.month and today.day < nacimiento.day):
            edad -= 1
        return edad
    except ValueError:
        return None

# Función para obtener el rango de edad (18-25, 25-35, 35-80)
def obtener_rango_edad(edad):
    """Devuelve el rango de edad al que pertenece una persona."""
    if edad < 25:
        return '18-25'
    elif edad < 35:
        return '25-35'
    elif edad <= 80:
        return '35-80'
    return None
