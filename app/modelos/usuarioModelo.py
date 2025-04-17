class Usuario:
    ORIENTACIONES_VALIDAS = {"heterosexual", "bisexual", "homosexual", "pansexual"}

    def __init__(self, id_usuario, nombre_usuario, contrasena, edad, genero, orientacion_sexual, bio, foto_perfil=None):
        if orientacion_sexual not in self.ORIENTACIONES_VALIDAS:
            raise ValueError("Orientación sexual no válida")
        
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.edad = edad
        self.genero = genero
        self.orientacion_sexual = orientacion_sexual
        self.bio = bio  # Nuevo campo para la biografía
        self.foto_perfil = foto_perfil  # Nuevo campo para la foto de perfil
    
    def a_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "contrasena": self.contrasena,
            "edad": self.edad,
            "genero": self.genero,
            "orientacion_sexual": self.orientacion_sexual,
            "bio": self.bio,  # Incluir la bio en el diccionario
            "foto_perfil": self.foto_perfil  # Incluir la foto de perfil en el diccionario
        }

    def actualizar(self, nombre_usuario=None, contrasena=None, edad=None, genero=None, orientacion_sexual=None, bio=None, foto_perfil=None):
        if nombre_usuario:
            self.nombre_usuario=nombre_usuario
        if contrasena:
            self.contrasena = contrasena
        if edad:
            self.edad = edad
        if genero:
            self.genero = genero
        if orientacion_sexual:
            if orientacion_sexual not in self.ORIENTACIONES_VALIDAS:
                raise ValueError("Orientación sexual no válida")
            self.orientacion_sexual = orientacion_sexual
        if bio is not None:  # Permitir la actualización de la bio
            self.bio = bio
        if foto_perfil:
            self.foto_perfil = foto_perfil  # Actualizar la foto de perfil