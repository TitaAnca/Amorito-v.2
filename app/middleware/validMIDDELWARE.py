from flask import request, jsonify
import re

def validar_registro(f):
    def decorador(*args, **kwargs):
        datos = request.get_json()

        if not datos:
            return jsonify({"error": "Se requiere un cuerpo JSON"}), 400

        if "email" not in datos or not re.match(r"[^@]+@[^@]+\.[^@]+", datos["email"]):
            return jsonify({"error": "Correo electrónico no válido"}), 400

        if "password" not in datos or len(datos["password"]) < 6:
            return jsonify({"error": "La contraseña debe tener al menos 6 caracteres"}), 400

        return f(*args, **kwargs)
    
    return decorador