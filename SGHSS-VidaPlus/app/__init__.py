from flask import Flask
from app.routes import auth_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    app.register_blueprint(auth_routes.bp)

    @app.route('/')
    def home():
        return "Olá, servidor está funcionando!"

    return app
