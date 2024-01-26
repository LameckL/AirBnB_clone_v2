#!/usr/bin/python3
"""starts a Flask web application

the appl listens on 0.0.0.0, port 5000
routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: Displays 'n is a number' only if <n> is an integer.
"""
from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """func displaying 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """func displaying 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """func displaying 'C' followed by the value of <text>

    it replaces any underscores in <text> with slashes
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """func displaying 'Python' followed by the value of <text>

    it replaces any underscores in <text> with slashes
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """func displaying 'n is a number' only if n is an integer"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
