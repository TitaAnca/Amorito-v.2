from flask import Blueprint
from app.controllers.autenticacionControl import registrar_usuario_controlador, iniciar_sesion_controlador

autent_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Rutas de autenticación
autent_bp.route('/registrar', methods=['POST'])(registrar_usuario_controlador)
autent_bp.route('/iniciar-sesion', methods=['POST'])(iniciar_sesion_controlador)
