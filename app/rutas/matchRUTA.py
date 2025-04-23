from flask import Blueprint
from app.controllers.matchControl import crear_match_controlador, obtener_compatibles_controlador, rechazar_match_controlador, obtener_matches_controlador

match_bp = Blueprint('match', __name__, url_prefix='/match')

@match_bp.route('/crear_match', methods=['POST'])
def crear_match():
    return crear_match_controlador()

@match_bp.route('/rechazar_match', methods=['POST'])
def rechazar_match():
    return rechazar_match_controlador()

@match_bp.route('/compatibles/<id_usuario>', methods=['GET'])
def obtener_compatibles(id_usuario):
    return obtener_compatibles_controlador(id_usuario)

@match_bp.route('/matches/<id_usuario>', methods=['GET'])
def obtener_matches(id_usuario):
    return obtener_matches_controlador(id_usuario)