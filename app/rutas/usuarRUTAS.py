from flask import Blueprint, request, jsonify
from modelos.usuarioModelo import Usuario
from utils import cargar_db, guardar_db

usuario_bp = Blueprint('usuarios', __name__)

# 📌 Obtener todos los usuarios
@usuario_bp.route('/', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.obtener_todos()
    return jsonify(usuarios)

# 📌 Obtener un usuario por ID
@usuario_bp.route('/<int:id_usuario>', methods=['GET'])
def obtener_usuario(id_usuario):
    usuario = Usuario.obtener_por_id(id_usuario)
    if usuario:
        return jsonify(usuario)
    return jsonify({"mensaje": "Usuario no encontrado"}), 404

# 📌 Crear un nuevo usuario
@usuario_bp.route('/crear', methods=['POST'])
def crear_usuario():
    datos = request.get_json()
    db = cargar_db()

    # Verificar si el usuario ya existe
    if any(user['username'] == datos['username'] for user in db['usuarios']):
        return jsonify({"mensaje": "El usuario ya existe"}), 400

    nuevo_usuario = Usuario(
        id_usuario=len(db["usuarios"]) + 1,
        username=datos["username"],
        contrasena=datos["password"],
        edad=datos["edad"],
        genero=datos["genero"],
    )

    nuevo_usuario.guardar()
    return jsonify({"mensaje": "Usuario creado con éxito", "id_usuario": nuevo_usuario.id_usuario})

# 📌 Eliminar un usuario
@usuario_bp.route('/eliminar/<int:id_usuario>', methods=['DELETE'])
def eliminar_usuario(id_usuario):
    usuario = Usuario.obtener_por_id(id_usuario)
    if usuario:
        Usuario.eliminar(id_usuario)
        return jsonify({"mensaje": "Usuario eliminado correctamente"})
    return jsonify({"mensaje": "Usuario no encontrado"}), 404
