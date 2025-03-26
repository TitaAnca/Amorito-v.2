from flask import jsonify
from app.services.usuarioServicio import obtener_usuario_por_nombre, eliminar_usuario

def actualizar_usuario_controlador():
    datos = request.get_json()
    nombre_usuario = datos.get("nombre_usuario")
    contrasena = datos.get("contrasena")
    edad = datos.get("edad")
    genero = datos.get("genero")

    # Verificar si el nombre de usuario está presente
    if not nombre_usuario:
        return jsonify({"mensaje": "El nombre de usuario es obligatorio"}), 400

    if actualizar_usuario(nombre_usuario, contrasena, edad, genero):
        return jsonify({"mensaje": "Datos del usuario actualizados correctamente"}), 200
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

def obtener_usuario_controlador(nombre_usuario):
    usuario = obtener_usuario_por_nombre(nombre_usuario)
    if usuario:
        return jsonify(usuario), 200  # Si lo encuentra, devuelve los datos
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404  # Si no lo encuentra, mensaje de error

def eliminar_usuario_controlador(nombre_usuario):
    if eliminar_usuario(nombre_usuario):
        return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200
    else:
        return jsonify({"mensaje": "No se pudo eliminar el usuario"}), 400