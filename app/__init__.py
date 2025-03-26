from flask import Flask
from app.rutas.usuarRUTAS import usuario_bp
from app.rutas.mesjRUTA import mensaje_bp
from app.rutas.matchRUTA import match_bp
from app.rutas.autenRUTA import autent_bp
from app.config import DevelopmentConfig  # Aquí importas la configuración

def create_app():
    # Crear la instancia de la aplicación Flask
    app = Flask(__name__)

    # Configuración de la aplicación (puedes cargar distintas configuraciones)
    app.config.from_object(DevelopmentConfig)  # Aquí cargamos la configuración del entorno

    # Registrar las rutas
    app.register_blueprint(usuario_bp)
    app.register_blueprint(mensaje_bp)
    app.register_blueprint(match_bp)
    app.register_blueprint(autent_bp)

    return app
