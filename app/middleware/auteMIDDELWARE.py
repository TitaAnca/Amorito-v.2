import jwt
from flask import request, jsonify
from functools import wraps
from app.config import SECRET_KEY

def verificar_token(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token or not token.startswith("Bearer "):
            return jsonify({"error": "Token no proporcionado o inválido"}), 401

        try:
            token = token.split(" ")[1]  # Eliminar el prefijo "Bearer"
            datos = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.usuario_id = datos["usuario_id"]
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token inválido"}), 401

        return f(*args, **kwargs)

    return decorador