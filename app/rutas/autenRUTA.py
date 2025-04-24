from flask import Blueprint, render_template
from app.controllers.autenticacionControl import registrar_usuario_controlador, iniciar_sesion_controlador

# Define el Blueprint para las rutas de autenticación
autent_bp = Blueprint('auth', __name__, url_prefix='/auth')

@autent_bp.route('/', methods=['GET'])
def mostrar_registro():
    print("Accediendo a la página de registro")  # Ver si la ruta está siendo alcanzada
    return render_template('Registro.html')

autent_bp.route('/registrar', methods=['POST'])(registrar_usuario_controlador)
autent_bp.route('/iniciar-sesion', methods=['POST'])(iniciar_sesion_controlador)
