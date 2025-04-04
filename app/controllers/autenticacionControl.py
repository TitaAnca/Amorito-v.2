from flask import request, jsonify
from werkzeug.utils import secure_filename
import _osx_support
from app.servicios.usuarioServicio import registrar_usuario, iniciar_sesion

# Ruta de registro
def registrar_usuario_controlador():
    datos = request.get_json()

    # Validar la entrada
    if not datos.get("nombre_usuario") or not datos.get("contrasena") or not datos.get("edad") or not datos.get("genero") or not datos.get("id_usuario") or not datos.get("orientacion_sexual"):
        return jsonify({"mensaje": "El nombre de usuario, la contraseña, la edad, el género y la orientación sexual son obligatorios"}), 400
    
    id_usuario = datos.get("id_usuario")
    nombre_usuario = datos.get("nombre_usuario")
    contrasena = datos.get("contrasena")
    try:
        edad = int(datos.get("edad"))
    except ValueError:
        return jsonify({"mensaje": "La edad debe ser un número válido"}), 400
    genero = datos.get("genero")
    orientacion_sexual = datos.get("orientacion_sexual")

    # Validar que la orientación sexual esté en los valores permitidos
    if orientacion_sexual not in ["heterosexual", "bisexual", "homosexual", "pansexual"]:
        return jsonify({"mensaje": "La orientación sexual no es válida"}), 400

    foto = request.files.get("foto_perfil")  # Aquí obtenemos el archivo de la foto de perfil
    # Registrar al usuario
    if registrar_usuario(id_usuario, nombre_usuario, contrasena, edad, genero, orientacion_sexual):
        return jsonify({"mensaje": "Usuario registrado correctamente"}), 201
    else:
        return jsonify({"mensaje": "El usuario ya existe o los datos no son válidos"}), 400

# Ruta de inicio de sesión
def iniciar_sesion_controlador():
    datos = request.get_json()

    # Validar la entrada
    if not datos.get("id_usuario") or not datos.get("contrasena"):
        return jsonify({"mensaje": "El nombre de usuario y la contraseña son obligatorios"}), 400

    id_usuario = datos.get("nombre_usuario")
    contrasena = datos.get("contrasena")

    # Verificar si el inicio de sesión es exitoso
    if iniciar_sesion(id_usuario, contrasena):
        return jsonify({"mensaje": "Inicio de sesión exitoso"}), 200
    else:
        return jsonify({"mensaje": "Usuario o contraseña incorrectos"}), 401
