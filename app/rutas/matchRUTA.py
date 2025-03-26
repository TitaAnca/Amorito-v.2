from flask import Blueprint, request, jsonify
from utils import cargar_db, guardar_db

match_bp = Blueprint('matches', __name__)

# 📌 Crear un match entre dos usuarios
@match_bp.route('/crear', methods=['POST'])
def crear_match():
    datos = request.get_json()
    db = cargar_db()

    # Verificar si los usuarios existen
    usuario1 = next((user for user in db['usuarios'] if user["id"] == datos["id_usuario1"]), None)
    usuario2 = next((user for user in db['usuarios'] if user["id"] == datos["id_usuario2"]), None)

    if not usuario1 or not usuario2:
        return jsonify({"mensaje": "Uno o ambos usuarios no existen"}), 404

    # Verificar si el match ya existe
    for match in db["matches"]:
        if (match["id_usuario1"] == datos["id_usuario1"] and match["id_usuario2"] == datos["id_usuario2"]) or \
           (match["id_usuario1"] == datos["id_usuario2"] and match["id_usuario2"] == datos["id_usuario1"]):
            return jsonify({"mensaje": "El match ya existe"}), 400

    nuevo_match = {
        "id_usuario1": datos["id_usuario1"],
        "id_usuario2": datos["id_usuario2"]
    }

    db["matches"].append(nuevo_match)
    guardar_db(db)
    
    return jsonify({"mensaje": "Match"})

# 📌 Obtener todos los matches de un usuario
@match_bp.route('/usuario/<int:id_usuario>', methods=['GET'])
def obtener_matches(id_usuario):
    db = cargar_db()
    matches = [
        match for match in db["matches"]
        if match["id_usuario1"] == id_usuario or match["id_usuario2"] == id_usuario
    ]
    
    return jsonify(matches)

# 📌 Eliminar un match
@match_bp.route('/eliminar', methods=['POST'])
def eliminar_match():
    datos = request.get_json()
    db = cargar_db()

    nuevo_lista_matches = [
        match for match in db["matches"]
        if not ((match["id_usuario1"] == datos["id_usuario1"] and match["id_usuario2"] == datos["id_usuario2"]) or
                (match["id_usuario1"] == datos["id_usuario2"] and match["id_usuario2"] == datos["id_usuario1"]))
    ]

    if len(nuevo_lista_matches) == len(db["matches"]):
        return jsonify({"mensaje": "No Match"}), 404

    db["matches"] = nuevo_lista_matches
    guardar_db(db)

    return jsonify({"mensaje": "Match Eliminado"})
