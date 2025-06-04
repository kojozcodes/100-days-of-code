from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """This is my first flask app."""
    return "<p>Hello, World!</p>"
