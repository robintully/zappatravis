from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Servers are dead, Long live Traviz Lambda!"