from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hey Scott, come hack me bro!"
