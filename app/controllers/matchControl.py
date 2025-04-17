from app.servicios.matchServicio import crear_match
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
        return jsonify({"mensaje": "Match creada exitosamente", "match": match.to_dict()}), 201
    else:
        return jsonify({"error": "No se encontró un match (verifica edad, preferencias y compatibilidad de género)"}), 400
