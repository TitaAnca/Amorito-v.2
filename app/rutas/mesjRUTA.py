from flask import Blueprint
from app.controllers.mensajeControl import enviar_mensaje, obtener_mensajes

ruta_mensajes = Blueprint('mensajes', __name__)

ruta_mensajes.route('/enviar', methods=['POST'])(enviar_mensaje)
ruta_mensajes.route('/obtener', methods=['GET'])(obtener_mensajes)
