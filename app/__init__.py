from flask import Flask, render_template
from app.rutas.usuarRUTAS import usuario_bp
from app.rutas.mesjRUTA import mensaje_bp
from app.rutas.matchRUTA import match_bp
from app.rutas.autenRUTA import autent_bp
from app.config import DevelopmentConfig

def create_app():
    # Crear la instancia de la aplicación Flask
    app = Flask(__name__,
                static_folder="../static",  # Archivos estáticos (CSS, JS)
                template_folder="../templates")  # Plantillas HTML

    # Configuración de la aplicación (Cargar configuración del entorno)
    @app.route('/')
    def index():
        return render_template('Inicio.html')  # Cambiado a test.html para probar

    @app.route('/registro')
    def registrarse():
        return render_template('Registro.html')
    
    @app.route('/inicio_sesion')
    def iniciar_sesion():
        return render_template('Inicio_sesion.html')

    # Registrar los blueprints
    app.register_blueprint(usuario_bp)
    app.register_blueprint(mensaje_bp)
    app.register_blueprint(match_bp)
    app.register_blueprint(autent_bp)



    # Ruta principal que devuelve la página de registro

    return app

