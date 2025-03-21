from flask import Blueprint, request, jsonify
from app.utils.archivosUtils import cargar_datos, guardar_datos
from utils.validarUtils import validar_email, validar_contraseña

usuario_controller = Blueprint('usuario_controller', __name__)

@usuario_controller.route('registro/', methods=['POST'])
def registrar_usuario():
    # Recibir los datos del usuario en formato JSON
    data = request.get_json()

    # Verificar que todos los campos estén presentes
    if not data.get('nombre') or not data.get('email') or not data.get('contraseña'):
        return jsonify({"message": "Todos los campos son requeridos"}), 400

    # Validar el formato del email
    if not validar_email(data['email']):
        return jsonify({"message": "El formato del correo electrónico no es válido"}), 400

    # Validar la contraseña (mínimo 8 caracteres)
    if not validar_contraseña(data['contraseña']):
        return jsonify({"message": "La contraseña debe tener al menos 8 caracteres"}), 400

    # Cargar los usuarios desde el archivo JSON
    usuarios = cargar_datos('app/db/usuarios.json')

    # Verificar si el email ya está registrado
    for usuario in usuarios:
        if usuario['email'] == data['email']:
            return jsonify({"message": "El correo ya está registrado"}), 400
    
    # Crear un nuevo usuario
    nuevo_usuario = {
        "id": len(usuarios) + 1,  # Asignar un ID único, basado en el tamaño actual
        "nombre": data['nombre'],
        "email": data['email'],
        "contraseña": data['contraseña']  # En un entorno real, aquí deberías cifrar la contraseña
    }

    # Agregar el nuevo usuario a la lista de usuarios
    usuarios.append(nuevo_usuario)

    # Guardar los datos actualizados en el archivo JSON
    guardar_datos('app/db/usuarios.json', usuarios)

    # Devolver una respuesta con los datos del nuevo usuario
    return jsonify({
        "message": "Usuario registrado con éxito", 
        "usuario": nuevo_usuario
    }), 201

