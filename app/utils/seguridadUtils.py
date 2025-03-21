import bcrypt
def cifrar_contraseña(contraseña: str) -> str:
    """Cifra la contraseña usando bcrypt."""
    salt = bcrypt.gensalt()
    contraseña_cifrada = bcrypt.hashpw(contraseña.encode('utf-8'), salt)
    return contraseña_cifrada.decode('utf-8')

def verificar_contraseña(contraseña: str, contraseña_cifrada: str) -> bool:
    """Verifica si la contraseña proporcionada coincide con la cifrada."""
    return bcrypt.checkpw(contraseña.encode('utf-8'), contraseña_cifrada.encode('utf-8'))