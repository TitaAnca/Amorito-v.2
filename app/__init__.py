from flask import Flask
from .rutas.usuarRUTAS import usuario_bp
from .rutas.mesjRUTA import mensaje_bp
from .rutas.matchRUTA import match_bp
from .rutas.autenRUTA import autent_bp

def create_app():
    # Crear la instancia de la aplicación Flask
    app = Flask(__name__)

    # Configuración de la aplicación (puedes agregar configuraciones aquí)
    app.config['SECRET_KEY'] = 'mi_clave_secreta'  # Ejemplo de clave secreta para sesiones

    # Registrar las rutas
    app.register_blueprint(usuario_bp)
    app.register_blueprint(mensaje_bp)
    app.register_blueprint(match_bp)
    app.register_blueprint(autent_bp)

    return app
