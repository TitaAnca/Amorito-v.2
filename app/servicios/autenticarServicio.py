import bcrypt

class AuthService:
    @staticmethod
    def encriptar_contraseña(contraseña):
        """Hashea la contraseña antes de almacenarla."""
        salt = bcrypt.gensalt()  # Genera un salt aleatorio
        contraseña_hash = bcrypt.hashpw(contraseña.encode('utf-8'), salt)
        return contraseña_hash.decode('utf-8')  # Convertir a string para almacenar en DB

    @staticmethod
    def verificar_contraseña(contraseña, contraseña_hash):
        """Verifica si la contraseña ingresada coincide con la almacenada."""
        return bcrypt.checkpw(contraseña.encode('utf-8'), contraseña_hash.encode('utf-8'))
