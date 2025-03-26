class Usuario:
    def __init__(self, id_usuario, nombre_usuario, contrasena, edad, genero):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.edad = edad
        self.genero = genero

    def a_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "contrasena": self.contrasena,
            "edad": self.edad,
            "genero": self.genero
        }
