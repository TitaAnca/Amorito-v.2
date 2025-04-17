from app.modelos.matchModelo import Match
import json

def obtener_usuario_por_id(id_usuario):
    # Aquí buscamos el usuario por su ID en la base de datos, en este caso lo hacemos con JSON.
    with open('db/users.json') as f:
        usuarios = json.load(f)
    return next((usuario for usuario in usuarios if usuario['id_usuario'] == id_usuario), None)

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

def obtener_generos_atraidos(orientacion, genero_propio):
    if orientacion == "heterosexual":
        if genero_propio == "hombre":
            return ["mujer"]
        elif genero_propio == "mujer":
            return ["hombre"]
        elif genero_propio == "no binario":
            return ["hombre", "mujer"]
    elif orientacion == "homosexual":
        return [genero_propio]
    elif orientacion == "bisexual":
        return ["hombre", "mujer"]
    elif orientacion == "pansexual":
        return ["hombre", "mujer", "no binario"]
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
            if verificar_compatibilidad_edad(usuario, otro) and verificar_preferencias(usuario, otro):
                compatibles.append({
                    "id_usuario": otro['id_usuario'],
                    "nombre": otro['nombre_usuario'],
                    "edad": otro['edad'],
                    "genero": otro['genero'],
                    "foto_perfil": otro.get('foto_perfil', "https://via.placeholder.com/100"),
                    "bio": f"Soy {otro['nombre_usuario']}, podríamos conocernos."  # Puedes cambiar esto si tienes campo 'bio'
                })
    return compatibles

import os

def crear_match(id_usuario1, id_usuario2):
    usuario1 = obtener_usuario_por_id(id_usuario1)
    usuario2 = obtener_usuario_por_id(id_usuario2)

    if not usuario1 or not usuario2:
        return None

    matches_path = 'db/matches.json'
    matches = []

    # Cargar los matches existentes
    if os.path.exists(matches_path):
        with open(matches_path, 'r') as f:
            matches = [json.loads(line) for line in f if line.strip()]

    # ¿Ya existe un match inverso (el otro ya te dio like)?
    for match in matches:
        if match['id_usuario_1'] == id_usuario2 and match['id_usuario_2'] == id_usuario1:
            if match['estado'] == 'pendiente':
                match['estado'] = 'aceptado'
                # Sobrescribimos todo el archivo con el match actualizado
                with open(matches_path, 'w') as f:
                    for m in matches:
                        json.dump(m, f)
                        f.write('\n')
                return Match(id_usuario1, id_usuario2, 'aceptado', match['datos_match'])

            elif match['estado'] == 'aceptado':
                return Match(id_usuario1, id_usuario2, 'aceptado', match['datos_match'])

    # Si no existe el inverso, lo creamos como pendiente
    datos_match = {
        'edad_usuario1': usuario1['edad'],
        'edad_usuario2': usuario2['edad'],
        'preferencia_usuario1': usuario1['preferencia'],
        'preferencia_usuario2': usuario2['preferencia'],
        'genero_usuario1': usuario1['genero'],
        'genero_usuario2': usuario2['genero'],
    }

    nuevo_match = Match(id_usuario1, id_usuario2, 'pendiente', datos_match)

    with open(matches_path, 'a') as f:
        json.dump(nuevo_match.__dict__, f)
        f.write('\n')

    return nuevo_match
