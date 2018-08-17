'''the core application'''
from flask import Blueprint
from app.helper import rand_result

BLUEPRINT = Blueprint('BLUEPRINT', __name__)

@BLUEPRINT.route("/")
def hello():
    '''a route'''
    return str(rand_result())

@BLUEPRINT.route("/string")
def string():
    '''another route'''
    return 'cool it worked'
