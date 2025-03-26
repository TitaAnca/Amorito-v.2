from flask import Blueprint, request, jsonify
from app.controllers.mensajeControl import enviar_mensaje, obtener_mensajes

# Definir el Blueprint para mensajes
mensaje_bp = Blueprint('mensaje', __name__, url_prefix='/mensajes')

# Ruta para enviar un mensaje
@mensaje_bp.route('/enviar', methods=['POST'])
def enviar():
    datos = request.get_json()
    if not datos or 'remitente_id' not in datos or 'destinatario_id' not in datos or 'contenido' not in datos:
        return jsonify({'error': 'Faltan datos requeridos'}), 400
    
    respuesta = enviar_mensaje(datos['remitente_id'], datos['destinatario_id'], datos['contenido'])
    return jsonify(respuesta)

# Ruta para obtener mensajes de un usuario
@mensaje_bp.route('/<int:id_usuario>', methods=['GET'])
def obtener(id_usuario):
    mensajes = obtener_mensajes(id_usuario)
    return jsonify(mensajes)
