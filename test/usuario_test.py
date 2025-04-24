import unittest
from app import create_app

class UserTestCase(unittest.TestCase):

    def setUp(self):
        """Configuramos la aplicación para los tests."""
        self.app = create_app()
        self.client = self.app.test_client()

    def test_actualizar_usuario_exitoso(self):
        # Usamos la foto de perfil de Carlos
        with open('static/Imagenes/perfiles/carlitos123_perfil_prueba.jpg', 'rb') as foto:
            response = self.client.put('/usuario/actualizar', 
                data={
                    'id_usuario': 'carlitos123',  # ID del usuario a actualizar
                    'nombre_usuario': 'Carlos',
                    'contrasena': '67890',
                    'edad': '20',
                    'genero': 'masculino',
                    'orientacion_sexual': 'heterosexual',
                    'bio': 'Actualizando mi perfil!',
                    'foto_perfil': (foto, 'foto_perfil.jpg')  # Imagen real de Carlos
                }
            )
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('Datos del usuario actualizados correctamente', response.get_json()['mensaje'])

    def test_actualizar_usuario_datos_invalidos(self):
        """Prueba actualización con datos inválidos (nombre de usuario vacío)."""
        with open('static/Imagenes/perfiles/carlitos123_perfil_prueba.jpg', 'rb') as foto:
            response = self.client.put('/usuario/actualizar', 
                data={
                    'id_usuario': 'carlitos123',
                    'nombre_usuario': '',  # Nombre de usuario vacío, lo cual es inválido
                    'contrasena': '67890',
                    'edad': '20',
                    'genero': 'masculino',
                    'orientacion_sexual': 'heterosexual',
                    'bio': 'Actualizando mi perfil!',
                    'foto_perfil': (foto, 'foto_perfil.jpg')  # Imagen real de Carlos
                }
            )
        
        self.assertEqual(response.status_code, 400)
        self.assertIn('El nombre de usuario es obligatorio', response.get_json()['mensaje'])

    def test_actualizar_usuario_no_existente(self):
        """Prueba la actualización de un usuario que no existe."""
        with open('static/Imagenes/perfiles/carlitos123_perfil_prueba.jpg', 'rb') as foto:
            response = self.client.put('/usuario/actualizar', 
                data={
                    'id_usuario': 'usuario_inexistente',  # ID de usuario que no existe
                    'nombre_usuario': 'NoExistente',
                    'contrasena': '67890',
                    'edad': '20',
                    'genero': 'masculino',
                    'orientacion_sexual': 'heterosexual',
                    'bio': 'Este usuario no existe',
                    'foto_perfil': (foto, 'foto_perfil.jpg')  # Imagen real de Carlos
                }
            )
        
        self.assertEqual(response.status_code, 404)
        self.assertIn('Usuario no encontrado', response.get_json()['mensaje'])

if __name__ == "__main__":
    unittest.main()
