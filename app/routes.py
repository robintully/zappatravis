from flask import Flask
from .helper import rand_result

app = Flask(__name__)

@app.route("/")
def hello():
    return str(rand_result())