from app.modelos.matchModelo import Match
import json

def obtener_usuario_por_id(id_usuario):
    # Aquí buscamos el usuario por su ID en la base de datos, en este caso lo hacemos con JSON.
    with open('db/users.json') as f:
        usuarios = json.load(f)
    return next((usuario for usuario in usuarios if usuario['id'] == id_usuario), None)

def verificar_compatibilidad_edad(usuario1, usuario2):
    # Definimos los rangos de edad
    rangos_edad = [
        (18, 25),
        (25, 35),
        (35, 80),
    ]
    
    edad_usuario1 = usuario1['edad']
    edad_usuario2 = usuario2['edad']

    # Determinamos en qué rango de edad está cada uno
    rango_usuario1 = next((r for r in rangos_edad if r[0] <= edad_usuario1 <= r[1]), None)
    rango_usuario2 = next((r for r in rangos_edad if r[0] <= edad_usuario2 <= r[1]), None)

    # Comprobamos si ambos usuarios están en el mismo rango de edad
    return rango_usuario1 == rango_usuario2

def verificar_preferencias(usuario1, usuario2):
    # Comparar preferencias sexuales y géneros
    if usuario1['preferencia'] == usuario2['preferencia'] or usuario2['preferencia'] == "bisexual" or usuario1['preferencia'] == "bisexual":
        if usuario1['genero'] == usuario2['genero'] or usuario2['genero'] == "no binario" or usuario1['genero'] == "no binario":
            return True
    return False

def crear_match(id_usuario1, id_usuario2):
    # Buscar los usuarios
    usuario1 = obtener_usuario_por_id(id_usuario1)
    usuario2 = obtener_usuario_por_id(id_usuario2)

    if not usuario1 or not usuario2:
        return None

    # Verificar compatibilidad de edades
    if not verificar_compatibilidad_edad(usuario1, usuario2):
        return None  # Si no son compatibles por edad, no creamos la match

    # Verificar preferencias y géneros
    if not verificar_preferencias(usuario1, usuario2):
        return None  # Si no son compatibles por preferencia, no creamos la match

    # Crear la match
    datos_match = {
        'edad_usuario1': usuario1['edad'],
        'edad_usuario2': usuario2['edad'],
        'preferencia_usuario1': usuario1['preferencia'],
        'preferencia_usuario2': usuario2['preferencia'],
        'genero_usuario1': usuario1['genero'],
        'genero_usuario2': usuario2['genero'],
    }
    nuevo_match = Match(id_usuario1, id_usuario2, 'pendiente', datos_match)

    # Guardar la match en la base de datos
    with open('db/matches.json', 'a') as f:
        json.dump(nuevo_match.__dict__, f)
        f.write('\n')

    return nueva_match