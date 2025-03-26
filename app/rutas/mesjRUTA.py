from flask import Blueprint, request, jsonify
from utils import cargar_db, guardar_db

mensajes_bp = Blueprint('mensajes', __name__)

# 📌 Enviar un mensaje entre usuarios
@mensajes_bp.route('/enviar', methods=['POST'])
def enviar_mensaje():
    datos = request.get_json()
    db = cargar_db()

    # Verificar que los usuarios existen
    usuario1 = next((user for user in db['usuarios'] if user["id"] == datos["remitente"]), None)
    usuario2 = next((user for user in db['usuarios'] if user["id"] == datos["destinatario"]), None)

    if not usuario1 or not usuario2:
        return jsonify({"mensaje": "Uno o ambos usuarios no existen"}), 404

    nuevo_mensaje = {
        "remitente": datos["remitente"],
        "destinatario": datos["destinatario"],
        "contenido": datos["contenido"]
    }

    db["mensajes"].append(nuevo_mensaje)
    guardar_db(db)
    
    return jsonify({"mensaje": "Mensaje enviado con éxito"})

# 📌 Obtener mensajes entre dos usuarios
@mensajes_bp.route('/conversacion/<int:id_usuario1>/<int:id_usuario2>', methods=['GET'])
def obtener_conversacion(id_usuario1, id_usuario2):
    db = cargar_db()
    mensajes = [
        msg for msg in db["mensajes"]
        if (msg["remitente"] == id_usuario1 and msg["destinatario"] == id_usuario2) or 
           (msg["remitente"] == id_usuario2 and msg["destinatario"] == id_usuario1)
    ]
    
    return jsonify(mensajes)

# 📌 Eliminar un mensaje (opcional, si se necesita)
@mensajes_bp.route('/eliminar/<int:index>', methods=['DELETE'])
def eliminar_mensaje(index):
    db = cargar_db()

    if 0 <= index < len(db["mensajes"]):
        db["mensajes"].pop(index)
        guardar_db(db)
        return jsonify({"mensaje": "Mensaje eliminado con éxito"})
    
    return jsonify({"mensaje": "Mensaje no encontrado"}), 404
