import os

class Config:
    """Clase base para la configuración de la aplicación."""
    # Clave secreta para manejar sesiones y cookies
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mi_clave_secreta')  # Se puede cambiar para producción
    # Ruta del archivo JSON para la base de datos simulada
    DATABASE_PATH = 'data/base_datos.json'
    
    # Configuración para la carga de archivos
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/Imagenes/perfiles')  # Ruta donde se almacenarán las fotos
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limitar el tamaño máximo de los archivos a 16MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}  # Tipos de archivos permitidos

class DevelopmentConfig(Config):
    """Configuración específica para el entorno de desarrollo."""
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    """Configuración específica para el entorno de producción."""
    DEBUG = False
    ENV = 'production'
    # Aquí podrías agregar configuraciones como conexión a bases de datos reales
    # DATABASE_URI = os.environ.get('DATABASE_URI') 

class TestingConfig(Config):
    """Configuración específica para el entorno de pruebas."""
    DEBUG = True
    TESTING = True
    ENV = 'testing'

