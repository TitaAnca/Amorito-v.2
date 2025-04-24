from flask import Blueprint, request, jsonify
from app.controllers.usuarioControl import (
    actualizar_usuario_controlador,
    obtener_usuario_controlador,
    eliminar_usuario_controlador
)

usuario_bp = Blueprint('usuario_bp', __name__, url_prefix='/usuario')


@usuario_bp.route('/actualizar', methods=['PUT'])
def actualizar_usuario():
    return actualizar_usuario_controlador()
usuario_bp.route('/obtener/<string:id_usuario>', methods=['GET'])(obtener_usuario_controlador)
usuario_bp.route('/eliminar/<string:id_usuario>', methods=['DELETE'])(eliminar_usuario_controlador)
