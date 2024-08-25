from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simulador.db'
    app.config['SECRET_KEY'] = 'secret_key'
    
    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    return app
