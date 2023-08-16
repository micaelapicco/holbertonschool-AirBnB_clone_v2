#!/usr/bin/python3
"""Task 5:
Say hello and connect port
"""
from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """say hello"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """say hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text_c(text):
    """say c + text"""
    correct_format = text.replace("_", " ")
    return "C " + correct_format


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_python(text):
    """say python + text or python is cool"""
    correct_format = text.replace("_", " ")
    return "Python " + correct_format


@app.route('/number/<int:n>', strict_slashes=False)
def number_int(n):
    """display n is a number if n is an integer"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display n template if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
