import json
from app.models.usuarioModelo import Usuario

# Leer los usuarios desde el archivo JSON
def obtener_todos_usuarios():
    try:
        with open('db/usuarios.json', 'r') as archivo:
            return json.load(archivo)
    except Exception as e:
        raise Exception(f"Error al leer el archivo de usuarios: {str(e)}")

# Guardar los usuarios en el archivo JSON
def guardar_usuarios(usuarios):
    try:
        with open('db/usuarios.json', 'w') as archivo:
            json.dump(usuarios, archivo, indent=4)
    except Exception as e:
        raise Exception(f"Error al guardar el archivo de usuarios: {str(e)}")

# Validar el género
def validar_genero(genero):
    if genero not in ["masculino", "femenino", "no binario"]:
        return False
    return True

# Registrar un nuevo usuario
def registrar_usuario(nombre_usuario, contrasena, edad, genero):
    if not validar_genero(genero):
        return False  # Género no válido

    usuarios = obtener_todos_usuarios()

    # Verificar si el usuario ya existe
    if any(usuario['nombre_usuario'] == nombre_usuario for usuario in usuarios):
        return False  # El usuario ya existe

    # Crear el nuevo usuario
    nuevo_usuario = Usuario(nombre_usuario, contrasena, edad, genero)
    usuarios.append(nuevo_usuario.a_dict())
    guardar_usuarios(usuarios)
    return True

# Iniciar sesión (verificar usuario y contraseña)
def iniciar_sesion(nombre_usuario, contrasena):
    usuarios = obtener_todos_usuarios()

    # Buscar el usuario
    usuario = next((usuario for usuario in usuarios if usuario['nombre_usuario'] == nombre_usuario), None)

    if usuario and usuario['contrasena'] == contrasena:
        return True
    return False
