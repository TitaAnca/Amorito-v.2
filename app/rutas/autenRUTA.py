from flask import Blueprint
from app.controllers.authControlador import registrar_usuario_controlador, iniciar_sesion_controlador

auth_bp = Blueprint('auth', __name__)

# Rutas de autenticación
auth_bp.route('/registrar', methods=['POST'])(registrar_usuario_controlador)
auth_bp.route('/iniciar-sesion', methods=['POST'])(iniciar_sesion_controlador)
