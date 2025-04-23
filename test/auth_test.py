import unittest
from app import create_app

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_login_correcto(self):
        response = self.client.post('/login', json={
            'email': 'usuario@ejemplo.com',
            'password': 'clavecorrecta'
        })
        self.assertIn(response.status_code, [200, 201])

    def test_login_incorrecto(self):
        response = self.client.post('/login', json={
            'email': 'usuario@ejemplo.com',
            'password': 'claveincorrecta'
        })
        self.assertIn(response.status_code, [401, 403])

if __name__ == '__main__':
    unittest.main()