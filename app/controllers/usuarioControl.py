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

