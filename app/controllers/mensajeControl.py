from flask import request, jsonify
from app.servicios.mensajeServicio import enviar_mensaje, obtener_conversacion

def enviar_mensaje_controlador():
    try:
        data = request.form or request.json
        id_emisor = data.get("id_emisor")
        id_receptor = data.get("id_receptor")
        contenido = data.get("contenido")

        if not id_emisor or not id_receptor or not contenido:
            return jsonify({"mensaje": "Datos incompletos"}), 400

        enviar_mensaje(id_emisor, id_receptor, contenido)
        return jsonify({"mensaje": "Mensaje enviado"}), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 403
    except Exception as e:
        return jsonify({"error": "Error al enviar mensaje", "detalle": str(e)}), 500

def obtener_conversacion_controlador(id_usuario_1, id_usuario_2):
    try:
        mensajes = obtener_conversacion(id_usuario_1, id_usuario_2)
        return jsonify(mensajes), 200
    except Exception as e:
        return jsonify({"error": "Error al obtener la conversación", "detalle": str(e)}), 500
