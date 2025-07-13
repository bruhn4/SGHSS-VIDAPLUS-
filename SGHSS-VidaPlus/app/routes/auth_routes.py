from flask import Blueprint, request
from app.controllers import auth_controller

bp = Blueprint('auth_routes', __name__)

@bp.route('/login', methods=['POST'])
def login():
    return auth_controller.login(request)
@bp.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    return auth_controller.cadastrar_usuario(request)
@bp.route('/usuarios/<int:id>', methods=['PUT'])
def editar_usuario(id):
    return auth_controller.editar_usuario(request, id)
