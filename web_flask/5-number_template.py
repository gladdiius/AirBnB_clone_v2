#!/usr/bin/python3
"""
This script starts a Flask web application.
The web application listens on 0.0.0.0, port 5000.
Routes:
  - /: displays "Hello HBNB!"
  - /hbnb: displays "HBNB"
  - /c/<text>: displays "C ", followed by the value of the text variable
    (replace underscore (_) symbols with a space)
  - /python/<text>: displays "Python ", followed by the value of the text variable
    (replace underscore (_) symbols with a space)
    The default value of text is "is cool".
  - /number/<n>: displays "n is a number" only if n is an integer.
  - /number_template/<n>: displays an HTML page only if n is an integer:
    H1 tag: "Number: n" inside the BODY tag.
Options:
  - Uses the option strict_slashes=False in route definitions.
  - Adheres to PEP 8 style (version 1.7).
"""

from flask import Flask, render_template

app = Flask(__name__)

# Define a route for the home page
@app.route('/', strict_slashes=False)
def home():
    """
    Displays "Hello HBNB!" for the home route.
    """
    return 'Hello HBNB!'

# Define a route for /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays "HBNB" for the /hbnb route.
    """
    return 'HBNB'

# Define a route for /c/<text>
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays "C ", followed by the value of the text variable.
    Replaces underscore (_) symbols with a space.
    """
    return 'C {}'.format(text.replace('_', ' '))

# Define a route for /python/<text>
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Displays "Python ", followed by the value of the text variable.
    Replaces underscore (_) symbols with a space.
    The default value of text is "is cool".
    """
    return 'Python {}'.format(text.replace('_', ' '))

# Define a route for /number/<n>
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays "n is a number" only if n is an integer.
    """
    return '{} is a number'.format(n)

# Define a route for /number_template/<n>
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays an HTML page with H1 tag: "Number: n" inside the BODY tag,
    only if n is an integer.
    """
    return render_template('5-number.html', number=n)

if __name__ == '__main__':
    # Run the application on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)

