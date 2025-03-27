from flask import Blueprint
from app.controllers.matchControl import crear_match_controlador

match_bp = Blueprint('match', __name__, url_prefix='/match')

# Ruta para crear una nueva coincidencia
@match_bp.route('/crear_match', methods=['POST'])
def crear_match():
    return crear_match_controlador()