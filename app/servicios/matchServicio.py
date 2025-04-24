from app.modelos.matchModelo import Match
import json
import os

MATCHES_DB_PATH = "db/matches.json"

def cargar_matches():
    try:
        with open(MATCHES_DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def obtener_usuarios_con_match(id_usuario):
    matches = cargar_matches()
    usuarios = []
    for match in matches:
        if match["estado"] == "aceptado":
            if match["id_usuario_1"] == id_usuario:
                usuarios.append(match["id_usuario_2"])
            elif match["id_usuario_2"] == id_usuario:
                usuarios.append(match["id_usuario_1"])
    return usuarios

def obtener_usuario_por_id(id_usuario):
    with open('db/usuarios.json') as f:
        usuarios = json.load(f)
    return next((usuario for usuario in usuarios if usuario['id_usuario'] == id_usuario), None)

def actualizar_matches(matches): #guardar cambios
    try:
        with open('db/matches.json', 'w') as f:
            json.dump(matches, f, indent=4)
    except Exception as e:
        raise Exception(f"Error al guardar el archivo de usuarios: {str(e)}")
    
def ya_existe_match_o_rechazo(id1, id2):
    matches_path = 'db/matches.json'
    
    # Cargar matches existentes
    matches = []
    if os.path.exists(matches_path):
        with open(matches_path, 'r') as f:
            matches = json.load(f)
    for match in matches:
        if (
            (match["id_usuario_1"] == id1 and match["id_usuario_2"] == id2) or
            (match["id_usuario_1"] == id2 and match["id_usuario_2"] == id1)
        ) and match["estado"] in ["aceptado", "rechazado"]:
            return True
    return False

def tiene_match(id1, id2):
    matches_path = 'db/matches.json'
    matches = []
    if os.path.exists(matches_path):
        with open(matches_path, 'r') as f:
            matches = json.load(f)
    for match in matches:
        if (
            (match["id_usuario_1"] == id1 and match["id_usuario_2"] == id2) or
            (match["id_usuario_1"] == id2 and match["id_usuario_2"] == id1)
        ) and match["estado"] in ["aceptado"]:
            return True
    return False


def verificar_compatibilidad_edad(usuario1, usuario2):
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

    return rango_usuario1 == rango_usuario2 #devuelve true o false

def obtener_generos_atraidos(orientacion, genero_propio):
    if orientacion == "heterosexual":
        if genero_propio == "masculino":
            return ["femenino"]
        elif genero_propio == "femenino":
            return ["masculino"]
        elif genero_propio == "no binario":
            return ["masculino", "femenino"]
    elif orientacion == "homosexual":
        return [genero_propio]
    elif orientacion == "bisexual":
        return ["masculino", "femenino"]
    elif orientacion == "pansexual":
        return ["masculino", "femenino", "no binario"]
    return []

def verificar_preferencias(usuario1, usuario2):
    generos_usuario1 = obtener_generos_atraidos(usuario1['orientacion_sexual'], usuario1['genero'])
    generos_usuario2 = obtener_generos_atraidos(usuario2['orientacion_sexual'], usuario2['genero'])

    return (usuario2['genero'] in generos_usuario1) and (usuario1['genero'] in generos_usuario2)


def obtener_usuarios_compatibles(id_usuario):
    usuario = obtener_usuario_por_id(id_usuario)
    if not usuario:
        return []

    with open('db/usuarios.json') as f:
        todos = json.load(f)

    compatibles = []
    for otro in todos:
        if otro['id_usuario'] != id_usuario:
            if ya_existe_match_o_rechazo(id_usuario, otro['id_usuario']):
                continue

            if verificar_compatibilidad_edad(usuario, otro) and verificar_preferencias(usuario, otro):
                compatibles.append({
                    "id_usuario": otro.get('id_usuario'),
                    "nombre": otro.get('nombre_usuario'),
                    "edad": otro.get('edad'),
                    "genero": otro.get('genero'),
                    "foto_perfil": otro.get('foto_perfil', "https://via.placeholder.com/100"),
                    "bio": otro.get('bio')
                })

    return compatibles

def crear_match(id_usuario1, id_usuario2):
    usuario1 = obtener_usuario_por_id(id_usuario1)
    usuario2 = obtener_usuario_por_id(id_usuario2)

    if not usuario1 or not usuario2:
        return None

    matches_path = 'db/matches.json'
    matches = []
    if os.path.exists(matches_path):
        with open(matches_path, 'r') as f:
            matches = json.load(f)

    # match inverso?
    if matches: 
        for match in matches:
            if match['id_usuario_1'] == id_usuario2 and match['id_usuario_2'] == id_usuario1:
                if match['estado'] == 'pendiente':
                    match['estado'] = 'aceptado'
                    actualizar_matches(matches) 
                    return Match(id_usuario1, id_usuario2, 'aceptado', match['datos_match'])
                elif match['estado'] == 'pendienteRechazo':
                    match['estado'] = 'rechazado'
                    actualizar_matches(matches)
                    return Match(id_usuario1, id_usuario2, 'rechazado', match['datos_match'])

    # Si no existe el inverso, lo creamos como pendiente
    datos_match = {
        'edad_usuario1': usuario1['edad'],
        'edad_usuario2': usuario2['edad'],
        'preferencia_usuario1': usuario1['orientacion_sexual'],
        'preferencia_usuario2': usuario2['orientacion_sexual'],
        'genero_usuario1': usuario1['genero'],
        'genero_usuario2': usuario2['genero'],
    }

    nuevo_match = Match(id_usuario1, id_usuario2, 'pendiente', datos_match)
    matches.append(nuevo_match.__dict__)
    actualizar_matches(matches)
    return nuevo_match


def rechazar_match(id_usuario1, id_usuario2):
    usuario1 = obtener_usuario_por_id(id_usuario1)
    usuario2 = obtener_usuario_por_id(id_usuario2)

    if not usuario1 or not usuario2:
        return None

    matches_path = 'db/matches.json'
    matches = []
    if os.path.exists(matches_path):
        with open(matches_path, 'r') as f:
            matches = json.load(f)

    for match in matches:
        if match['id_usuario_1'] == id_usuario2 and match['id_usuario_2'] == id_usuario1:
            if match['estado'] == 'pendiente':
                match['estado'] = 'rechazado'
                actualizar_matches(matches)
                return Match(id_usuario1, id_usuario2, 'rechazado', match['datos_match'])
            elif match['estado'] == 'pendienteRechazo':
                match['estado'] = 'rechazado'
                actualizar_matches(matches)
                return Match(id_usuario1, id_usuario2, 'rechazado', match['datos_match'])

    # Si no existe el inverso, lo creamos como pendiente de rechazo
    datos_match = {
        'edad_usuario1': usuario1['edad'],
        'edad_usuario2': usuario2['edad'],
        'preferencia_usuario1': usuario1['orientacion_sexual'],
        'preferencia_usuario2': usuario2['orientacion_sexual'],
        'genero_usuario1': usuario1['genero'],
        'genero_usuario2': usuario2['genero'],
    }

    nuevo_match = Match(id_usuario1, id_usuario2, 'pendienteRechazo', datos_match)
    matches.append(nuevo_match.__dict__)
    actualizar_matches(matches)
    return nuevo_match