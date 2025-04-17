from app.servicios.matchServicio import crear_match, obtener_usuarios_compatibles
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
        else:
            return jsonify({
                "mensaje": "Aún no ha habido respuesta del otro usuario",
                "match": match.to_dict()
            }), 200
    else:
        return jsonify({"error": "Error al intentar hacer match"}), 400

def obtener_compatibles_controlador(id_usuario):
    compatibles = obtener_usuarios_compatibles(id_usuario)
    return jsonify(compatibles)