#!/usr/bin/python3
"""
This script starts a Flask web application.
The web application listens on 0.0.0.0, port 5000.
Routes:
  - /: displays "Hello HBNB!"
  - /hbnb: displays "HBNB"
  - /c/<text>: displays "C " followed by the value of the text variable
    (replace underscore _ symbols with a space)
Options:
  - Uses the option strict_slashes=False in route definitions.
  - Adheres to PEP 8 style (version 1.7).
"""

from flask import Flask, render_template
import re

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
    Displays "C " followed by the value of the text variable.
    Replaces underscore (_) symbols with a space.
    """
    cleaned_text = re.sub('_', ' ', text)
    return 'C {}'.format(cleaned_text)

if __name__ == '__main__':
    # Run the application on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
