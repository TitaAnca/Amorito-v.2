import jwt
import datetime
from app.config import SECRET_KEY  # Asegúrate de tener tu clave secreta en un archivo de configuración seguro.

def generar_token(usuario_id: int) -> str:
    """Genera un token JWT para un usuario."""
    payload = {
        'usuario_id': usuario_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expira en 1 hora
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def verificar_token(token: str) -> dict:
    """Verifica la validez de un token JWT y devuelve el payload decodificado."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return {"message": "El token ha expirado"}
    except jwt.InvalidTokenError:
        return {"message": "Token inválido"}