from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from app.config import Config
import json
import os

USUARIOS_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'usuarios.json')

def carregar_usuarios():
    if not os.path.exists(USUARIOS_FILE):
        with open(USUARIOS_FILE, 'w') as f:
            json.dump([], f)
    with open(USUARIOS_FILE, 'r') as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open(USUARIOS_FILE, 'w') as f:
        json.dump(usuarios, f, indent=4)

def get_usuarios():
    return carregar_usuarios()

def cadastrar_usuario(request):
    usuarios = carregar_usuarios()
    dados = request.get_json()
    campos_necessarios = ["nome", "email", "senha", "perfil"]
    if not dados or not all(campo in dados for campo in campos_necessarios):
        return jsonify({"message": "Dados incompletos para cadastro."}), 400

    if any(u['email'].lower() == dados['email'].lower() for u in usuarios):
        return jsonify({"message": "Email já cadastrado."}), 409

    senha_criptografada = generate_password_hash(dados['senha'])
    novo_id = max([u['id'] for u in usuarios], default=0) + 1

    usuario = {
        "id": novo_id,
        "nome": dados['nome'],
        "email": dados['email'],
        "senha": senha_criptografada,
        "senha_original": dados['senha'],  # obs: nunca armazenar senhas em texto plano em sistemas reais!
        "perfil": dados['perfil']
    }

    usuarios.append(usuario)
    salvar_usuarios(usuarios)

    print("Usuário cadastrado:", usuario)
    return jsonify(usuario), 201

def login(request):
    usuarios = carregar_usuarios()
    dados = request.get_json()
    print("Dados recebidos no login:", dados)

    usuario = next((u for u in usuarios if u['email'].lower() == dados['email'].lower()), None)
    print("Usuário encontrado:", usuario)

    if usuario:
        senha_valida = check_password_hash(usuario['senha'], dados['senha'])
        print("Senha válida?", senha_valida)

        if senha_valida:
            token = jwt.encode({
                'id': usuario['id'],
                'exp': datetime.utcnow() + timedelta(hours=1)
            }, Config.SECRET_KEY, algorithm="HS256")
            print("Login OK, token gerado")
            return jsonify({"token": token}), 200
        else:
            print("Senha inválida")
    else:
        print("Usuário não encontrado")

    return jsonify({"message": "Credenciais inválidas!"}), 401

def editar_usuario(request, id):
    usuarios = carregar_usuarios()
    dados = request.get_json()
    
    usuario = next((u for u in usuarios if u['id'] == id), None)
    
    if not usuario: 
        return jsonify({"message": "Usuário não encontado!"}), 404
    
    if 'nome' in dados:
        usuario['nome'] = dados['nome']
    if 'email' in dados:
        if any(u for u in usuarios if u['email'].lower() == dados['email'].lower() and u['id'] != id):
            return jsonify({"message": "Este e-mail está sendo usado por outro usuário!"}), 409
        usuario['email'] = dados['email']
    if 'senha' in dados:
        usuario['senha'] = generate_password_hash(dados['senha'])
        usuario['senha_original'] = dados['senha']
    
    salvar_usuarios(usuarios)
    return jsonify({"message": "Informações atualizadas com sucesso!", "usuario": usuario}), 200