from app.modelos.matchModelo import Match
from app.modelos.usuarioModelo import Usuario
from app.controllers.matchControl import MatchControl

class MatchServicio:
    @staticmethod
    def crear_match(id_usuario1, id_usuario2):
        """Crea un match entre dos usuarios si están en el mismo rango de edad."""
        usuario1 = Usuario.obtener_usuario(id_usuario1)
        usuario2 = Usuario.obtener_usuario(id_usuario2)

        if not usuario1 or not usuario2:
            return {"mensaje": "Uno o ambos usuarios no existen"}, 404

        # Determinar los rangos de edad de los usuarios
        rango1 = MatchControl.obtener_rango_edad(usuario1["edad"])
        rango2 = MatchControl.obtener_rango_edad(usuario2["edad"])

        # Si los rangos no coinciden, no se puede hacer un match
        if rango1 != rango2:
            return {"mensaje": "Los usuarios no están en el mismo rango de edad"}, 400

        # Crear y guardar el nuevo match
        match = Match(id_usuario1, id_usuario2)
        return match.guardar()

    @staticmethod
    def obtener_matches(id_usuario):
        """Obtiene todos los matches de un usuario."""
        matches = Match.obtener_matches(id_usuario)
        return matches if matches else {"mensaje": "No hay matches para este usuario"}

    @staticmethod
    def eliminar_match(id_usuario1, id_usuario2):
        """Elimina un match entre dos usuarios."""
        return Match.eliminar_match(id_usuario1, id_usuario2)
