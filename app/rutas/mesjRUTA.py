from flask import Blueprint
from app.controllers.mensajeControl import enviar_mensaje_controlador, obtener_conversacion_controlador

mensaje_bp = Blueprint("mensaje", __name__, url_prefix="/mensaje")

@mensaje_bp.route("/enviar_mensaje", methods=["POST"])
def enviar():
    return enviar_mensaje_controlador()

@mensaje_bp.route("/conversacion/<id_usuario_1>/<id_usuario_2>", methods=["GET"])
def conversacion(id_usuario_1, id_usuario_2):
    return obtener_conversacion_controlador(id_usuario_1, id_usuario_2)
