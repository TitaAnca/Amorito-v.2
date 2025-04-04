class Usuario:
    ORIENTACIONES_VALIDAS = {"heterosexual", "bisexual", "homosexual", "pansexual"}

    def __init__(self, id_usuario, nombre_usuario, contrasena, edad, genero, orientacion_sexual, foto_perfil=None):
        if orientacion_sexual not in self.ORIENTACIONES_VALIDAS:
            raise ValueError("Orientación sexual no válida")
        
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.edad = edad
        self.genero = genero
        self.orientacion_sexual = orientacion_sexual
        self.foto_perfil = foto_perfil  # Nuevo campo para la foto de perfil
    
    def a_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "contrasena": self.contrasena,
            "edad": self.edad,
            "genero": self.genero,
            "orientacion_sexual": self.orientacion_sexual,
            "foto_perfil": self.foto_perfil  # Incluir la foto de perfil en el diccionario
        }

    def actualizar(self, contrasena=None, edad=None, genero=None, orientacion_sexual=None, foto_perfil=None):
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
        if foto_perfil:
            self.foto_perfil = foto_perfil  # Actualizar la foto de perfil

    
    def es_match(self, otro_usuario):
        if not isinstance(otro_usuario, Usuario):
            return False
        
        # Definimos compatibilidad de acuerdo a la orientación sexual
        if self.orientacion_sexual == "heterosexual":
            return self.genero != otro_usuario.genero and (otro_usuario.orientacion_sexual in {"heterosexual", "bisexual"})
        elif self.orientacion_sexual == "homosexual":
            return self.genero == otro_usuario.genero and (otro_usuario.orientacion_sexual in {"homosexual", "bisexual"})
        elif self.orientacion_sexual == "bisexual":
            return otro_usuario.orientacion_sexual in {"heterosexual", "homosexual", "bisexual", "pansexual"}
        elif self.orientacion_sexual == "pansexual":
            return True  # Puede coincidir con cualquier orientación
        
        return False