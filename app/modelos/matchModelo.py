import json
from utils import cargar_db, guardar_db
from modelos.usuarioModelo import Usuario

class Match:
    def __init__(self, id_usuario1, id_usuario2):
        self.id_usuario1 = id_usuario1
        self.id_usuario2 = id_usuario2

    def obtener_rango_edad(self, edad):
        """Determina el rango de edad del usuario."""
        if 18 <= edad <= 25:
            return "18-25"
        elif 26 <= edad <= 35:
            return "26-35"
        elif 36 <= edad <= 80:
            return "36-80"
        return None

    def guardar(self):
        db = cargar_db()

        # Obtener la información de los usuarios
        usuario1 = next((user for user in db["usuarios"] if user["id"] == self.id_usuario1), None)
        usuario2 = next((user for user in db["usuarios"] if user["id"] == self.id_usuario2), None)

        if not usuario1 or not usuario2:
            return {"mensaje": "Uno o ambos usuarios no existen"}, 404

        # Obtener los rangos de edad de ambos usuarios
        rango1 = self.obtener_rango_edad(usuario1["edad"])
        rango2 = self.obtener_rango_edad(usuario2["edad"])

        if rango1 != rango2:
            return {"mensaje": "Los usuarios no están en el mismo rango de edad"}, 400

        # Verificar si el match ya existe
        for match in db["matches"]:
            if (match["id_usuario1"] == self.id_usuario1 and match["id_usuario2"] == self.id_usuario2) or \
               (match["id_usuario1"] == self.id_usuario2 and match["id_usuario2"] == self.id_usuario1):
                return {"mensaje": "El match ya existe"}

        db["matches"].append({
            "id_usuario1": self.id_usuario1,
            "id_usuario2": self.id_usuario2
        })
        guardar_db(db)
        return {"mensaje": "Match guardado con éxito"}

    @staticmethod
    def obtener_matches(id_usuario):
        """Obtiene todos los matches de un usuario."""
        db = cargar_db()
        return [
            match for match in db["matches"]
            if match["id_usuario1"] == id_usuario or match["id_usuario2"] == id_usuario
        ]

    @staticmethod
    def eliminar_match(id_usuario1, id_usuario2):
        """Elimina un match entre dos usuarios."""
        db = cargar_db()
        nuevo_lista_matches = [
            match for match in db["matches"]
            if not ((match["id_usuario1"] == id_usuario1 and match["id_usuario2"] == id_usuario2) or
                    (match["id_usuario1"] == id_usuario2 and match["id_usuario2"] == id_usuario1))
        ]

        if len(nuevo_lista_matches) == len(db["matches"]):
            return {"mensaje": "No se encontró el match"}, 404

        db["matches"] = nuevo_lista_matches
        guardar_db(db)
        return {"mensaje": "Match eliminado con éxito"}
