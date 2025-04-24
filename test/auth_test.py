import unittest
from io import BytesIO
from werkzeug.datastructures import FileStorage
from app import create_app

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        """Inicializa la aplicación y el cliente de pruebas."""
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_registro_correcto(self):
        """Prueba el registro de un nuevo usuario correctamente."""
        
        # Datos del formulario con un id_usuario único
        data = {
            'id_usuario': 'nuevo_usuario123',  # Asegúrate de que este usuario no exista en la base de datos
            'nombre_usuario': 'Nuevo Usuario',
            'contrasena': '12345',
            'edad': 25,
            'genero': 'masculino',
            'orientacion_sexual': 'heterosexual',
            'bio': 'Hola, soy nuevo aquí',
        }

        # Simulando la carga de una foto de perfil
        foto_perfil = FileStorage(
            stream=BytesIO(b"fake image content"), filename="nuevo_usuario123_perfil_prueba.jpg", content_type='image/jpeg'
        )
        
        # Agregamos la foto de perfil al formulario
        data['foto_perfil'] = foto_perfil

        # Hacemos el post a la ruta de registro
        response = self.client.post('/auth/registrar', data=data, content_type='multipart/form-data')

        # Depuración para ver qué devuelve la respuesta
        print(response.status_code)
        print(response.data)  # Imprimir el contenido de la respuesta para ver el mensaje de error

        # Verificamos que el registro haya sido exitoso
        self.assertEqual(response.status_code, 201)
        self.assertIn("Usuario registrado correctamente", response.get_json()['mensaje'])

    def test_login_correcto(self):
        """Prueba que el inicio de sesión funcione correctamente para un usuario existente."""
        
        # Datos de login
        login_data = {
            'id_usuario': 'carlitos123',  # Este debe ser un usuario que ya esté en tu base de datos
            'contrasena': '12345',  # Asegúrate de que este ID exista previamente en la base de datos
        }

        # Hacemos el post al login
        response = self.client.post('/auth/iniciar-sesion', json=login_data)

        # Verificamos que el login haya sido exitoso (302 si hay redirección)
        self.assertEqual(response.status_code, 302)

    def test_login_incorrecto(self):
        """Prueba que el inicio de sesión falle con credenciales incorrectas."""
        
        # Datos de login incorrectos
        login_data = {
            'id_usuario': 'carlitos123',  # Usuario correcto
            'contrasena': 'wrongpassword',  # Contraseña incorrecta
        }

        # Hacemos el post al login
        response = self.client.post('/auth/iniciar-sesion', json=login_data)

        # Verificamos que el login haya fallado (401 por usuario o contraseña incorrectos)
        self.assertEqual(response.status_code, 401)
        self.assertIn("Usuario o contraseña incorrectos", response.get_json()['mensaje'])

if __name__ == '__main__':
    unittest.main()
