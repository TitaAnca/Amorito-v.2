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
    def iniciarSesion():
        return render_template('Inicio_sesion.html')

    @app.route('/matches/<id_usuario>')
    def matches(id_usuario):
        # Aquí puedes cargar los datos específicos del usuario con el id_usuario
        return render_template('Matches.html', id_usuario=id_usuario)
    @app.route('/perfil/<id_usuario>')
    def mostrar_perfil(id_usuario):
        return render_template('perfil.html', id_usuario=id_usuario)
    
    @app.route('/chat/<id_usuario>')
    def chat(id_usuario):
        return render_template('Chat.html', id_usuario=id_usuario)
    # Registrar los blueprints
    app.register_blueprint(usuario_bp)
    app.register_blueprint(mensaje_bp)
    app.register_blueprint(match_bp)
    app.register_blueprint(autent_bp)



    # Ruta principal que devuelve la página de registro

    return app
