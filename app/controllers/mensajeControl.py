from modelos.mensajeModelo import Mensaje

class MensajeControl:
    @staticmethod
    def enviar_mensaje(remitente, destinatario, contenido):
        """Envía un mensaje entre dos usuarios."""
        nuevo_mensaje = Mensaje(remitente, destinatario, contenido)
        nuevo_mensaje.guardar()
        return {"mensaje": "Mensaje enviado con éxito", "timestamp": nuevo_mensaje.timestamp}

    @staticmethod
    def obtener_conversacion(id_usuario1, id_usuario2):
        """Obtiene todos los mensajes entre dos usuarios."""
        mensajes = Mensaje.obtener_conversacion(id_usuario1, id_usuario2)
        return mensajes if mensajes else {"mensaje": "No hay mensajes entre estos usuarios"}

    @staticmethod
    def eliminar_mensaje(index):
        """Elimina un mensaje por su índice en la base de datos."""
        if Mensaje.eliminar_mensaje(index):
            return {"mensaje": "Mensaje eliminado con éxito"}
        return {"mensaje": "Mensaje no encontrado"}, 404