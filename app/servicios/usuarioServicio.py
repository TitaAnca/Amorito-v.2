import os
import json
from werkzeug.utils import secure_filename
from app.modelos.usuarioModelo import Usuario

# Configuración de la ruta para guardar fotos
UPLOAD_FOLDER = 'static/Imagenes/perfiles'

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
    if edad < 18 or edad > 90:
        return False
    return True

# Validar la orientación sexual
def validar_orientacion(orientacion):
    if orientacion not in ["heterosexual", "bisexual", "homosexual", "pansexual"]:
        return False
    return True

def guardar_foto_perfil(foto, id_usuario):
    if foto:
        filename = secure_filename(foto.filename)  # Asegurarse de que el nombre del archivo sea seguro
        foto_path = os.path.join(UPLOAD_FOLDER, f"{id_usuario}_{filename}")
        foto.save(foto_path)  # Guardamos la foto en el directorio correspondiente
        return foto_path  # Devolvemos la ruta de la foto guardada
    return None  # Si no hay foto, retornamos None

# Registrar un nuevo usuario
def registrar_usuario(id_usuario, nombre_usuario, contrasena, edad, genero, orientacion_sexual, bio, foto=None):
    if not validar_genero(genero) or not validar_edad(edad) or not validar_orientacion(orientacion_sexual):
        return False  # Datos no válidos

    usuarios = obtener_todos_usuarios()

    # Verificar si el usuario ya existe
    if any(usuario['id_usuario'] == id_usuario for usuario in usuarios):
        return False  # El usuario ya existe

    foto_perfil = None
    if foto:
        foto_perfil = guardar_foto_perfil(foto, id_usuario)

    # Crear el nuevo usuario
    nuevo_usuario = Usuario(id_usuario, nombre_usuario, contrasena, edad, genero, orientacion_sexual, bio, foto_perfil)
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

def obtener_usuario_por_nombre(id_usuario):
    usuarios = obtener_todos_usuarios()
    usuario = next((usuario for usuario in usuarios if usuario['id_usuario'] == id_usuario), None)
    return usuario

def actualizar_usuario(id_usuario, nombre_usuario, contrasena=None, edad=None, genero=None, orientacion_sexual=None, bio=None, foto=None):
    usuarios = obtener_todos_usuarios()

    # Buscar el usuario
    usuario = next((usuario for usuario in usuarios if usuario['id_usuario'] == id_usuario), None)

    if not usuario:
        return False  # Usuario no encontrado

    usuario_obj = Usuario(**usuario)
    usuario_obj.actualizar(nombre_usuario, contrasena, edad, genero, orientacion_sexual)

    if bio is not None:  # Solo actualizamos la bio si se proporciona
        usuario_obj.actualizar(bio=bio)

    if foto:
        foto_perfil = guardar_foto_perfil(foto, id_usuario)
        usuario_obj.actualizar(foto_perfil=foto_perfil)
        
    # Guardar los usuarios actualizados
    usuarios = [usuario_obj.a_dict() if usuario['id_usuario'] == id_usuario else usuario for usuario in usuarios]

    guardar_usuarios(usuarios)
    
    return True

# Eliminar un usuario por ID
def eliminar_usuario(id_usuario):
    usuarios = obtener_todos_usuarios()

    # Buscar el índice del usuario en la lista
    usuario_a_eliminar = next((usuario for usuario in usuarios if usuario['id_usuario'] == id_usuario), None)

    if usuario_a_eliminar:
        usuarios.remove(usuario_a_eliminar)  # Eliminar el usuario de la lista
        guardar_usuarios(usuarios)  # Guardar el archivo actualizado
        return True
    else:
        return False  # Si no se encuentra el usuario, no se puede eliminar