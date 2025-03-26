from app.modelos.mensajeModelo import Mensaje
import json
import os

class ServicioMensaje:
    def __init__(self):
        self.ruta_db = 'app/db/messages.json'

    def crear_mensaje(self, id_emisor, id_receptor, contenido, timestamp):
        mensaje = Mensaje(id_emisor, id_receptor, contenido, timestamp)
        if self.guardar_mensaje(mensaje):
            return mensaje
        return None

    def guardar_mensaje(self, mensaje):
        try:
            mensajes = self.cargar_mensajes()
            mensajes.append(mensaje.a_dict())
            with open(self.ruta_db, 'w') as f:
                json.dump(mensajes, f)
            return True
        except Exception as e:
            print(f"Error guardando mensaje: {e}")
            return False

    def cargar_mensajes(self):
        if os.path.exists(self.ruta_db):
            with open(self.ruta_db, 'r') as f:
                return json.load(f)
        return []

    def obtener_mensajes(self, id_emisor, id_receptor):
        mensajes = self.cargar_mensajes()
        mensajes_filtrados = [
            mensaje for mensaje in mensajes
            if (mensaje['id_emisor'] == id_emisor and mensaje['id_receptor'] == id_receptor) or
               (mensaje['id_emisor'] == id_receptor and mensaje['id_receptor'] == id_emisor)
        ]
        return [Mensaje(m['id_emisor'], m['id_receptor'], m['contenido'], m['timestamp']) for m in mensajes_filtrados]
