from modelos.matchModelo import Match
from modelos.usuarioModelo import Usuario

class MatchControl:
    @staticmethod
    def obtener_rango_edad(edad):
        """Determina el rango de edad del usuario."""
        if 18 <= edad <= 25:
            return "18-25"
        elif 26 <= edad <= 35:
            return "26-35"
        elif 36 <= edad <= 80:
            return "36-80"
        return None

    @staticmethod
    def crear_match(id_usuario1, id_usuario2):
        """Crea un match entre dos usuarios solo si están en el mismo rango de edad."""
        usuario1 = Usuario.obtener_usuario(id_usuario1)
        usuario2 = Usuario.obtener_usuario(id_usuario2)

        if not usuario1 or not usuario2:
            return {"mensaje": "Uno o ambos usuarios no existen"}, 404

        rango1 = MatchControl.obtener_rango_edad(usuario1["edad"])
        rango2 = MatchControl.obtener_rango_edad(usuario2["edad"])

        if rango1 != rango2:
            return {"mensaje": "Los usuarios no están en el mismo rango de edad"}, 400

        nuevo_match = Match(id_usuario1, id_usuario2)
        return nuevo_match.guardar()

    @staticmethod
    def obtener_matches(id_usuario):
        """Obtiene la lista de matches de un usuario."""
        matches = Match.obtener_matches(id_usuario)
        return matches if matches else {"mensaje": "No hay matches para este usuario"}

    @staticmethod
    def eliminar_match(id_usuario1, id_usuario2):
        """Elimina un match entre dos usuarios."""
        return Match.eliminar_match(id_usuario1, id_usuario2)
