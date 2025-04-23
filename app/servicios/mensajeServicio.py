import json
import os
from datetime import datetime
from app.modelos.mensajeModelo import Mensaje
from app.servicios.matchServicio import tiene_match

MENSAJES_PATH = "db/mensajes.json"

def cargar_mensajes():
    if not os.path.exists(MENSAJES_PATH):
        return []
    with open(MENSAJES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_mensajes(mensajes):
    with open(MENSAJES_PATH, "w", encoding="utf-8") as f:
        json.dump(mensajes, f, ensure_ascii=False, indent=4)

def enviar_mensaje(id_emisor, id_receptor, contenido):
    if not tiene_match(id_emisor, id_receptor):
        raise ValueError("No puedes enviar mensajes a alguien con quien no tienes match")

    mensajes = cargar_mensajes()
    nuevo_mensaje = Mensaje(id_emisor, id_receptor, contenido, datetime.now().isoformat())
    mensajes.append(nuevo_mensaje.a_dict())
    guardar_mensajes(mensajes)
    return True

def obtener_conversacion(id_usuario_1, id_usuario_2):
    mensajes = cargar_mensajes()
    return [
        m for m in mensajes
        if (m["id_emisor"] == id_usuario_1 and m["id_receptor"] == id_usuario_2)
        or (m["id_emisor"] == id_usuario_2 and m["id_receptor"] == id_usuario_1)
    ]
