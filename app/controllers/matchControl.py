from app.servicios.matchServicio import crear_match, rechazar_match, obtener_usuarios_compatibles, obtener_usuarios_con_match
from flask import jsonify, request

def crear_match_controlador():
    id_usuario1 = request.json.get('id_usuario1')
    id_usuario2 = request.json.get('id_usuario2')

    if not id_usuario1 or not id_usuario2:
        return jsonify({"error": "Ambos ID de usuario son requeridos"}), 400

    if id_usuario1 == id_usuario2:
        return jsonify({"error": "Un usuario no puede hacer match consigo mismo"}), 400

    match = crear_match(id_usuario1, id_usuario2)

    if match:
        if match.estado == "aceptado":
            return jsonify({
                "mensaje": "¡Es un match!",
                "match": match.to_dict()
            }), 201
        elif match.estado == "pendienteRechazo":
            return jsonify({
                "mensaje": "No hay match :(",
                "match": match.to_dict()
            }), 200
        else:
            return jsonify({
                "mensaje": "Esperando respuesta",
                "match": match.to_dict()
            }), 200
    else:
        return jsonify({"error": "Error al intentar hacer match"}), 400
    
def rechazar_match_controlador():
    id_usuario1 = request.json.get('id_usuario1')
    id_usuario2 = request.json.get('id_usuario2')

    # Validación de los ID de usuario
    if not id_usuario1 or not id_usuario2:
        return jsonify({"error": "Ambos ID de usuario son requeridos"}), 400

    if id_usuario1 == id_usuario2:
        return jsonify({"error": "Un usuario no puede rechazar a sí mismo"}), 400

    # Intentar rechazar el match
    match = rechazar_match(id_usuario1, id_usuario2)

    if match:
        return jsonify({
            "mensaje": "No hay match :(",
            "match": match.to_dict()
        }), 200
    else:
        return jsonify({"error": "Error al intentar rechazar el match"}), 400


def obtener_compatibles_controlador(id_usuario):
    compatibles = obtener_usuarios_compatibles(id_usuario)
    return jsonify(compatibles)

def obtener_matches_controlador(id_usuario):
    try:
        usuarios_con_match = obtener_usuarios_con_match(id_usuario)
        return jsonify(usuarios_con_match), 200
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener matches", "error": str(e)}), 500