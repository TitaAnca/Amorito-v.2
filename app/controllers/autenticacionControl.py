from flask import request, jsonify
from app.servicios.usuarioServicio import registrar_usuario, iniciar_sesion

# Ruta de registro
def registrar_usuario_controlador():
    datos = request.get_json()

    # Validar la entrada
    if not datos.get("nombre_usuario") or not datos.get("contrasena") or not datos.get("edad") or not datos.get("genero") or not datos.get("id_usuario"):
        return jsonify({"mensaje": "El nombre de usuario, la contraseña, la edad y el género son obligatorios"}), 400
    
    id_usuario = datos.get("id_usuario")
    nombre_usuario = datos.get("nombre_usuario")
    contrasena = datos.get("contrasena")
    edad = datos.get("edad")
    genero = datos.get("genero")

    # Registrar al usuario
    if registrar_usuario(id_usuario , nombre_usuario, contrasena, edad, genero):
        return jsonify({"mensaje": "Usuario registrado correctamente"}), 201
    else:
        return jsonify({"mensaje": "El usuario ya existe o el género no es válido"}), 400

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
