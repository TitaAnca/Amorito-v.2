class Usuario:
    def __init__(self, nombre_usuario, contrasena, edad, genero):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.edad = edad
        self.genero = genero

    def a_dict(self):
        return {
            "nombre_usuario": self.nombre_usuario,
            "contrasena": self.contrasena,
            "edad": self.edad,
            "genero": self.genero
        }
    def actualizar(self, contrasena=None, edad=None, genero=None):
    if contrasena:
        self.contrasena = contrasena
    if edad:
        self.edad = edad
    if genero:
        self.genero = genero
