from flask import request, jsonify
from app.services.messageService import ServicioMensaje
from datetime import datetime

servicio_mensaje = ServicioMensaje()

def enviar_mensaje():
    datos = request.get_json()

    id_emisor = datos.get('id_emisor')
    id_receptor = datos.get('id_receptor')
    contenido = datos.get('contenido')

    if not id_emisor or not id_receptor or not contenido:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    timestamp = datetime.now().isoformat()
    mensaje = servicio_mensaje.crear_mensaje(id_emisor, id_receptor, contenido, timestamp)
    
    if mensaje:
        return jsonify(mensaje.a_dict()), 201
    return jsonify({"error": "No se pudo crear el mensaje"}), 500

def obtener_mensajes():
    id_emisor = request.args.get('id_emisor')
    id_receptor = request.args.get('id_receptor')

    if not id_emisor or not id_receptor:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    mensajes = servicio_mensaje.obtener_mensajes(id_emisor, id_receptor)
    return jsonify([mensaje.a_dict() for mensaje in mensajes]), 200