from flask import Blueprint, request, jsonify
from controllers.matchControl import MatchControl

match_bp = Blueprint('match', __name__)

@match_bp.route('/crear', methods=['POST'])
def crear_match():
    """Crea un match entre dos usuarios solo si están en el mismo rango de edad."""
    datos = request.get_json()
    id_usuario1 = datos.get("id_usuario1")
    id_usuario2 = datos.get("id_usuario2")

    if not id_usuario1 or not id_usuario2:
        return jsonify({"mensaje": "Faltan los identificadores de los usuarios"}), 400

    respuesta = MatchControl.crear_match(id_usuario1, id_usuario2)
    return jsonify(respuesta)

@match_bp.route('/usuario/<int:id_usuario>', methods=['GET'])
def obtener_matches(id_usuario):
    """Obtiene todos los matches de un usuario."""
    respuesta = MatchControl.obtener_matches(id_usuario)
    return jsonify(respuesta)

@match_bp.route('/eliminar', methods=['POST'])
def eliminar_match():
    """Elimina un match entre dos usuarios."""
    datos = request.get_json()
    id_usuario1 = datos.get("id_usuario1")
    id_usuario2 = datos.get("id_usuario2")

    if not id_usuario1 or not id_usuario2:
        return jsonify({"mensaje": "Faltan los identificadores de los usuarios"}), 400

    respuesta = MatchControl.eliminar_match(id_usuario1, id_usuario2)
    return jsonify(respuesta)
