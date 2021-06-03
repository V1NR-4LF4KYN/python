#python3

# imports
from flask import Flask # the Flask-Class

# creating an instance of Flask()
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

