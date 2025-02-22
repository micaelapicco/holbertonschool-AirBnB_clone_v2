#!/usr/bin/python3
"""Task 8:
script that starts a Flask web application:
"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def remove_sql(remove):
    """remove the current SQLA session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states():
    """Display states"""
    all_states = storage.all(State).values()
    return render_template('7-states_list.html', all_states=all_states)


@app.route('/cities_by_states', strict_slashes=False)
def display_city():
    """Display cities"""
    all_states = storage.all(State).values()
    return render_template('8-cities_by_states.html', all_states=all_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
