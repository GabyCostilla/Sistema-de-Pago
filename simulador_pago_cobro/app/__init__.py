from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://uuvwhyajuwvidcnp:mPyc607HTrxFD0NCh66H@bk1ncwutzdrmggghixaa-mysql.services.clever-cloud.com:3306/bk1ncwutzdrmggghixaa'
    app.config['SECRET_KEY'] = 'mPyc607HTrxFD0NCh66H'
    
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Importa las rutas después de que `app` ha sido creado
    from . import routes

    return app
