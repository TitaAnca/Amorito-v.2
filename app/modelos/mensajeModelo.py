import json
from utils import cargar_db, guardar_db
from datetime import datetime

class Mensaje:
    def __init__(self, remitente, destinatario, contenido, timestamp=None):
        self.remitente = remitente
        self.destinatario = destinatario
        self.contenido = contenido
        self.timestamp = timestamp or datetime.utcnow().isoformat()

    def guardar(self):
        db = cargar_db()
        db["mensajes"].append({
            "remitente": self.remitente,
            "destinatario": self.destinatario,
            "contenido": self.contenido,
            "timestamp": self.timestamp
        })
        guardar_db(db)
        return self

    @staticmethod
    def obtener_conversacion(id_usuario1, id_usuario2):
        db = cargar_db()
        return [
            mensaje for mensaje in db["mensajes"]
            if (mensaje["remitente"] == id_usuario1 and mensaje["destinatario"] == id_usuario2) or
               (mensaje["remitente"] == id_usuario2 and mensaje["destinatario"] == id_usuario1)
        ]

    @staticmethod
    def eliminar_mensaje(index):
        db = cargar_db()
        if 0 <= index < len(db["mensajes"]):
            db["mensajes"].pop(index)
            guardar_db(db)
            return True
        return False
