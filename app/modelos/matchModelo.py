import json

archivo_db = "base_datos.json"  # Ruta del archivo JSON para simular la base de datos

class Match:
    def __init__(self, id_usuario1, id_usuario2):
        self.id_usuario1 = id_usuario1
        self.id_usuario2 = id_usuario2

    @staticmethod
    def cargar_db():
        """Carga la base de datos desde el archivo JSON."""
        try:
            with open(archivo_db, "r") as archivo:
                return json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"usuarios": [], "coincidencias": []}
    
    @staticmethod
    def guardar_db(datos):
        """Guarda los datos en el archivo JSON."""
        with open(archivo_db, "w") as archivo:
            json.dump(datos, archivo, indent=4)
    
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

    @classmethod
    def guardar(cls, self):
        """Guarda el match en la base de datos."""
        db = cls.cargar_db()
        # Verificar que no exista ya el match
        for match in db['coincidencias']:
            if (match['id_usuario1'] == self.id_usuario1 and match['id_usuario2'] == self.id_usuario2) or \
               (match['id_usuario1'] == self.id_usuario2 and match['id_usuario2'] == self.id_usuario1):
                return {"mensaje": "El match ya existe."}

        nuevo_match = {
            "id_usuario1": self.id_usuario1,
            "id_usuario2": self.id_usuario2
        }
        db['coincidencias'].append(nuevo_match)
        cls.guardar_db(db)
        return {"mensaje": "Match guardado con éxito"}

    @classmethod
    def obtener_matches(cls, id_usuario):
        """Obtiene todos los matches de un usuario."""
        db = cls.cargar_db()
        matches = [match for match in db['coincidencias'] if match['id_usuario1'] == id_usuario or match['id_usuario2'] == id_usuario]
        return matches

    @classmethod
    def eliminar_match(cls, id_usuario1, id_usuario2):
        """Elimina un match entre dos usuarios."""
        db = cls.cargar_db()
        match = next((m for m in db['coincidencias'] if m['id_usuario1'] == id_usuario1 and m['id_usuario2'] == id_usuario2), None)
        if not match:
            return {"mensaje": "El match no existe."}
        
        db['coincidencias'].remove(match)
        cls.guardar_db(db)
        return {"mensaje": "Match eliminado con éxito"}
