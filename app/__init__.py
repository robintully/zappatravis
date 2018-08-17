'''application factory'''
from flask import Flask
from app.routes import BLUEPRINT

def create_app():
    '''makes the application'''
    app = Flask(__name__)
    app.register_blueprint(BLUEPRINT)
    return app
