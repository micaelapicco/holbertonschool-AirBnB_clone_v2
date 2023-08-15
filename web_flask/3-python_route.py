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
    """when route is /c/<text> the display is display “C ”,
    followed by the value of the text variable"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text='is cool'):
    """when route is /python the display is “Python is cool”
    when route is /python/<text> the display is “Python ”,
    followed by the value of the text variable"""
    text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
