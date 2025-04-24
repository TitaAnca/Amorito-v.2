from flask import request, jsonify, redirect, url_for
from app.servicios.usuarioServicio import registrar_usuario, iniciar_sesion


def registrar_usuario_controlador():
    # Obtener los datos del formulario
    id_usuario = request.form.get('id_usuario')
    nombre_usuario = request.form.get('nombre_usuario')
    contrasena = request.form.get('contrasena')
    edad = request.form.get('edad')
    genero = request.form.get('genero')
    orientacion_sexual = request.form.get('orientacion_sexual')
    bio = request.form.get('bio')
    foto_perfil = request.files.get('foto_perfil') # Obtener la foto de perfil (si existe)

    # Validar la entrada
    if not id_usuario or not nombre_usuario or not contrasena or not edad or not genero or not orientacion_sexual or not bio or not foto_perfil:
        return jsonify({"mensaje": "El nombre de usuario, la contraseña, la edad, el género y la orientación sexual son obligatorios"}), 400

    # Validar la edad
    try:
        edad = int(edad)
    except ValueError:
        return jsonify({"mensaje": "La edad debe ser un número válido"}), 400

    # Registrar al usuario
    if registrar_usuario(id_usuario, nombre_usuario, contrasena, edad, genero, orientacion_sexual, bio, foto_perfil):
        return jsonify({"mensaje": "Usuario registrado correctamente"}), 201
    else:
        return jsonify({"mensaje": "El usuario ya existe o los datos no son válidos"}), 400

def iniciar_sesion_controlador():
    datos = request.get_json()

    # Validar la entrada
    if not datos.get("id_usuario") or not datos.get("contrasena"):
        return jsonify({"mensaje": "El nombre de usuario y la contraseña son obligatorios"}), 400

    id_usuario = datos.get("id_usuario")
    contrasena = datos.get("contrasena")

    # Verificar si el inicio de sesión es exitoso
    if iniciar_sesion(id_usuario, contrasena):
        return redirect(url_for('matches', id_usuario=id_usuario))
    else:
        return jsonify({"mensaje": "Usuario o contraseña incorrectos"}), 401