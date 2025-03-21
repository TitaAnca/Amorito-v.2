from flask import request, jsonify
from app.utils.tokenUtils import verificar_token

def autenticar_request():
    """Middleware para verificar que la solicitud tenga un token válido."""

    # Obtener el token del encabezado Authorization
    token = request.headers.get('Authorization')

    # Si no hay token en la solicitud, devolver un error
    if not token:
        return jsonify({"message": "Token no proporcionado"}), 401

    # Verificar el token
    resultado = verificar_token(token)

    if 'message' in resultado:  # Si hubo un error en la validación del token
        return jsonify(resultado), 401

    # Si el token es válido, agregar la información del usuario al contexto de la solicitud
    request.usuario_id = resultado['usuario_id']