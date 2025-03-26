from servicios.matchServicio import MatchServicio

class MatchControl:
    
    @staticmethod
    def crear_match(id_usuario1, id_usuario2):
        """Crea un match entre dos usuarios si están en el mismo rango de edad."""
        # Llamar al servicio para crear el match
        respuesta = MatchServicio.crear_match(id_usuario1, id_usuario2)
        
        # Si la respuesta es un error, devolver el error
        if isinstance(respuesta, dict) and "mensaje" in respuesta:
            return respuesta
        
        # Si el match se creó exitosamente
        return {"mensaje": "Match creado exitosamente"}
    
    @staticmethod
    def obtener_matches(id_usuario):
        """Obtiene todos los matches de un usuario."""
        matches = MatchServicio.obtener_matches(id_usuario)
        return matches
    
    @staticmethod
    def eliminar_match(id_usuario1, id_usuario2):
        """Elimina un match entre dos usuarios."""
        respuesta = MatchServicio.eliminar_match(id_usuario1, id_usuario2)
        
        # Si la respuesta es un mensaje de error, devolver el error
        if isinstance(respuesta, dict) and "mensaje" in respuesta:
            return respuesta
        
        # Si el match se eliminó con éxito
        return {"mensaje": "Match eliminado exitosamente"}
