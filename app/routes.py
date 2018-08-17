from flask import Flask
from .helper import rand_result

app = Flask(__name__)

@app.route("/")
def hello():
    return 'float'

@app.route("/string")
def string():
    return 'hello'