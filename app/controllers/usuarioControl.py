from flask import Blueprint, request, jsonify
from app.utils.archivosUtils import cargar_datos, guardar_datos
from utils.validarUtils import validar_email, validar_contraseña

usuario_controller = Blueprint('usuario_controller', __name__)

@usuario_controller.route('registro/', methods=['POST'])
def registrar_usuario():
    data = request.get_json()

    if not data.get('nombre') or not data.get('email') or not data.get('contraseña'):
        return jsonify({"message": "Todos los campos son requeridos"}), 400
    
    if not validar_email(data['email']):
        return jsonify({"message": "El formato del correo electrónico no es válido"}), 400

    if not validar_contraseña(data['contraseña']):
        return jsonify({"message": "La contraseña debe tener al menos 8 caracteres"}), 400
    
    usuarios = cargar_datos('app/db/usuarios.json')

    for usuario in usuarios:
        if usuario['email'] == data['email']:
            return jsonify({"message": "El correo ya está registrado"}), 400
    
    nuevo_usuario = {
        "id": len(usuarios) + 1,
        "nombre": data['nombre'],
        "email": data['email'],
        "contraseña": data['contraseña'] 
    }

    usuarios.append(nuevo_usuario)

    guardar_datos('app/db/usuarios.json', usuarios)

    return jsonify({
        "message": "Usuario registrado con éxito", 
        "usuario": nuevo_usuario
    }), 201


@usuario_controller.route('/login', methods=['POST'])
def login_usuario():
    # Recibir los datos del usuario en formato JSON
    data = request.get_json()

    # Validar que se hayan enviado los datos
    if not data.get('email') or not data.get('contraseña'):
        return jsonify({"message": "El correo y la contraseña son requeridos"}), 400

    usuarios = cargar_datos('app/db/usuarios.json')

    # Verificar si el email y la contraseña son correctos
    for usuario in usuarios:
        if usuario['email'] == data['email'] and usuario['contraseña'] == data['contraseña']:
            # Aquí deberías generar un token (JWT) en un entorno real
            return jsonify({"message": "Login exitoso", "usuario": usuario}), 200
    
    # Si no se encuentra el usuario o las credenciales son incorrectas
    return jsonify({"message": "Credenciales incorrectas"}), 401


# <form id="registroForm" action="/api/usuario/registrar" method="POST">
#   <input type="text" id="nombre" name="nombre" placeholder="Nombre" required>
#   <input type="email" id="email" name="email" placeholder="Correo electrónico" required> <!-- correo obligatorio -->
#   <input type="password" id="contraseña" name="contraseña" placeholder="Contraseña" required>
#   <button type="submit">Registrarse</button>
# </form> (MANERA DE HACER EL FORMULARIO)