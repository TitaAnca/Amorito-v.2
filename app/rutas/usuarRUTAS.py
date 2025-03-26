from flask import Blueprint
from app.controllers.usuarioControlador import registrar_usuario_controlador, iniciar_sesion_controlador, actualizar_usuario_controlador

usuario_bp = Blueprint('usuario_bp', __name__)

# Rutas de gestión de usuarios
usuario_bp.route('/actualizar', methods=['PUT'])(actualizar_usuario_controlador)  # Actualizar datos de usuario