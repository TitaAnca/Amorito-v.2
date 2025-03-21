import re

def validar_email(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email) is not None

def validar_contraseña(contraseña):
    if len(contraseña) >= 8:
        return True
    return False