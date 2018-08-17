'''the core application'''
from flask import Flask
from app.helper import rand_result

APP = Flask(__name__)

@APP.route("/")
def hello():
    '''a route'''
    return str(rand_result())

@APP.route("/string")
def string():
    '''another route'''
    return 'cool'
