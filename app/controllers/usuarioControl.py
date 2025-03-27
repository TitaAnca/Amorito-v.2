from flask import request, jsonify
from app.servicios.usuarioServicio import (
    obtener_usuario_por_nombre, 
    eliminar_usuario, 
    actualizar_usuario
)

def actualizar_usuario_controlador():
    datos = request.get_json()
    id_usuario = datos.get("id_usuario")
    nombre_usuario = datos.get("nombre_usuario")
    contrasena = datos.get("contrasena")
    edad = datos.get("edad")
    genero = datos.get("genero")
    orientacion_sexual = datos.get("orientacion_sexual")

    # Verificar si el ID de usuario está presente
    if not id_usuario:
        return jsonify({"mensaje": "El ID de usuario es obligatorio"}), 400

    if actualizar_usuario(id_usuario, contrasena, edad, genero, orientacion_sexual):
        return jsonify({"mensaje": "Datos del usuario actualizados correctamente"}), 200
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

def obtener_usuario_controlador(id_usuario):
    usuario = obtener_usuario_por_nombre(id_usuario)
    if usuario:
        return jsonify(usuario), 200  # Si lo encuentra, devuelve los datos
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404  # Si no lo encuentra, mensaje de error

def eliminar_usuario_controlador(id_usuario):
    if eliminar_usuario(id_usuario):
        return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200
    else:
        return jsonify({"mensaje": "No se pudo eliminar el usuario"}), 400
