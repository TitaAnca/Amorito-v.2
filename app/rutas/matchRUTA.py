from flask import Blueprint, request, jsonify
from servicios.matchServicio import MatchServicio

# Crear blueprint para las rutas de los matches
match_bp = Blueprint('match', __name__)

@match_bp.route('/crear', methods=['POST'])
def crear_match():
    """Crea un match entre dos usuarios solo si están en el mismo rango de edad."""
    datos = request.get_json()

    # Obtener los IDs de los usuarios
    id_usuario1 = datos.get("id_usuario1")
    id_usuario2 = datos.get("id_usuario2")

    if not id_usuario1 or not id_usuario2:
        return jsonify({"mensaje": "Faltan los identificadores de los usuarios"}), 400

    # Llamar al servicio para crear el match
    respuesta = MatchServicio.crear_match(id_usuario1, id_usuario2)
    return jsonify(respuesta)

@match_bp.route('/usuario/<int:id_usuario>', methods=['GET'])
def obtener_matches(id_usuario):
    """Obtiene todos los matches de un usuario."""
    matches = MatchServicio.obtener_matches(id_usuario)
    return jsonify(matches)

@match_bp.route('/eliminar', methods=['POST'])
def eliminar_match():
    """Elimina un match entre dos usuarios."""
    datos = request.get_json()

    id_usuario1 = datos.get("id_usuario1")
    id_usuario2 = datos.get("id_usuario2")

    if not id_usuario1 or not id_usuario2:
        return jsonify({"mensaje": "Faltan los identificadores de los usuarios"}), 400

    # Llamar al servicio para eliminar el match
    respuesta = MatchServicio.eliminar_match(id_usuario1, id_usuario2)
    return jsonify(respuesta)