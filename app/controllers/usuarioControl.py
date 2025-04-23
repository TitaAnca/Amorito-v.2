import os
from flask import request, jsonify
from werkzeug.utils import secure_filename
from app.servicios.usuarioServicio import (
    obtener_usuario_por_nombre, 
    eliminar_usuario, 
    actualizar_usuario
)

def actualizar_usuario_controlador():
    try:
        id_usuario = request.form.get("id_usuario")
        nombre_usuario = request.form.get("nombre_usuario")
        contrasena = request.form.get("contrasena")
        edad = request.form.get("edad")
        genero = request.form.get("genero")
        orientacion_sexual = request.form.get("orientacion_sexual")
        bio = request.form.get("bio")
        foto = request.files.get("foto_perfil")

        if not id_usuario:
            return jsonify({"mensaje": "El ID de usuario es obligatorio"}), 400

        resultado = actualizar_usuario(
            id_usuario, nombre_usuario, contrasena, int(edad) if edad else None,
            genero, orientacion_sexual, bio, foto
        )

        if resultado:
            return jsonify({"mensaje": "Datos del usuario actualizados correctamente"}), 200
        else:
            return jsonify({"mensaje": "Usuario no encontrado"}), 404

    except ValueError as ve:
        return jsonify({"mensaje": str(ve)}), 400
    except Exception as e:
        return jsonify({"mensaje": "Error al actualizar el usuario", "error": str(e)}), 500


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
