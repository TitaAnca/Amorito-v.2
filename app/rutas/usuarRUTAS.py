from flask import Blueprint
from app.controllers.usuarioControlador import (
    actualizar_usuario_controlador,
    obtener_usuario_controlador,
    eliminar_usuario_controlador
)

usuario_bp = Blueprint('usuario_bp', __name__)

# Rutas de gestión de usuarios
usuario_bp.route('/actualizar', methods=['PUT'])(actualizar_usuario_controlador)  # Actualizar datos de usuario
usuario_bp.route('/obtener/<string:nombre_usuario>', methods=['GET'])(obtener_usuario_controlador)  # Ver perfil
usuario_bp.route('/eliminar/<string:nombre_usuario>', methods=['DELETE'])(eliminar_usuario_controlador)  # Eliminar cuenta
