from flask import Blueprint, request, jsonify
from app.servicios.autenticarServicio import registrar_usuario, autenticar_usuario

usuario_controller = Blueprint('usuario_controller', __name__)

@usuario_controller.route('/registro', methods=['POST'])
def registrar_usuario_api():
    data = request.get_json()

    # Validaciones de datos
    if not data.get('nombre') or not data.get('email') or not data.get('contraseña'):
        return jsonify({"message": "Todos los campos son requeridos"}), 400
    
    # Registrar usuario llamando al servicio
    mensaje, status_code = registrar_usuario(data)

    return jsonify(mensaje), status_code

@usuario_controller.route('/login', methods=['POST'])
def login_usuario_api():
    data = request.get_json()

    # Validación de datos
    if not data.get('email') or not data.get('contraseña'):
        return jsonify({"message": "El correo y la contraseña son requeridos"}), 400

    # Autenticar usuario llamando al servicio
    mensaje, status_code = autenticar_usuario(data)

    return jsonify(mensaje), status_code


# <form id="registroForm" action="/api/usuario/registrar" method="POST">
#   <input type="text" id="nombre" name="nombre" placeholder="Nombre" required>
#   <input type="email" id="email" name="email" placeholder="Correo electrónico" required> <!-- correo obligatorio -->
#   <input type="password" id="contraseña" name="contraseña" placeholder="Contraseña" required>
#   <button type="submit">Registrarse</button>
# </form> (MANERA DE HACER EL FORMULARIO)