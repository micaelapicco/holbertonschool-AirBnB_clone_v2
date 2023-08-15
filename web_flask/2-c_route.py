#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """when route is / the display is Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """when route is /hbnb the display is HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """when route is /c/<text> the display is """
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
