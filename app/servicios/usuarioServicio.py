import json
from app.modelos.usuarioModelo import Usuario

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

def validar_edad(edad):
    if edad<18 and edad>90:
        return False
    return True

# Registrar un nuevo usuario
def registrar_usuario(id_usuario ,nombre_usuario, contrasena, edad, genero):
    if not validar_genero(genero):
        return False  # Género no válido

    if not validar_edad(edad):
        return False #Edad no válida

    usuarios = obtener_todos_usuarios()

    # Verificar si el usuario ya existe
    if any(usuario['nombre_usuario'] == id_usuario for usuario in usuarios):
        return False  # El usuario ya existe

    # Crear el nuevo usuario
    nuevo_usuario = Usuario(id_usuario, nombre_usuario, contrasena, edad, genero)
    usuarios.append(nuevo_usuario.a_dict())
    guardar_usuarios(usuarios)
    return True

# Iniciar sesión (verificar usuario y contraseña)
def iniciar_sesion(id_usuario, contrasena):
    usuarios = obtener_todos_usuarios()

    # Buscar el usuario
    usuario = next((usuario for usuario in usuarios if usuario['id_usuario'] == id_usuario), None)

    if usuario and usuario['contrasena'] == contrasena:
        return True
    return False

def obtener_usuario_por_nombre(nombre_usuario):
    usuarios = obtener_todos_usuarios()
    usuario = next((usuario for usuario in usuarios if usuario['nombre_usuario'] == nombre_usuario), None)
    return usuario

def actualizar_usuario(nombre_usuario, contrasena=None, edad=None, genero=None):
    usuarios = obtener_todos_usuarios()

    # Buscar el usuario
    usuario = next((usuario for usuario in usuarios if usuario['nombre_usuario'] == nombre_usuario), None)

    if not usuario:
        return False  # Usuario no encontrado

    usuario_obj = Usuario(**usuario)
    usuario_obj.actualizar(contrasena, edad, genero)

    # Guardar los usuarios actualizados
    usuarios = [usuario_obj.a_dict() if usuario['nombre_usuario'] == nombre_usuario else usuario for usuario in usuarios]
    guardar_usuarios(usuarios)
    
    return True