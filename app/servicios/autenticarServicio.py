from app.utils.seguridadUtils import cifrar_contraseña, verificar_contraseña
from app.utils.tokenUtils import generar_token
from app.utils.archivosUtils import cargar_datos, guardar_datos

def registrar_usuario(data):
    """Registra un nuevo usuario en el sistema."""
    usuarios = cargar_datos('app/db/usuarios.json')

    # Verificar si el correo ya está registrado
    for usuario in usuarios:
        if usuario['email'] == data['email']:
            return {"message": "El correo ya está registrado"}, 400

    # Cifrar la contraseña antes de almacenarla
    contraseña_cifrada = cifrar_contraseña(data['contraseña'])

    nuevo_usuario = {
        "id": len(usuarios) + 1,  # ID único basado en el número de usuarios
        "nombre": data['nombre'],
        "email": data['email'],
        "contraseña": contraseña_cifrada 
    }

    # Agregar el nuevo usuario a la lista de usuarios
    usuarios.append(nuevo_usuario)
    guardar_datos('app/db/usuarios.json', usuarios)

    return {"message": "Usuario registrado con éxito", "usuario": nuevo_usuario}, 201

def autenticar_usuario(data):
    """Verifica las credenciales del usuario y genera un token si son correctas."""
    usuarios = cargar_datos('app/db/usuarios.json')

    # Buscar al usuario por correo
    for usuario in usuarios:
        if usuario['email'] == data['email']:
            # Verificar la contraseña
            if verificar_contraseña(data['contraseña'], usuario['contraseña']):
                # Generar token JWT
                token = generar_token(usuario['id'])
                return {"message": "Login exitoso", "token": token}, 200

    return {"message": "Credenciales incorrectas"}, 401