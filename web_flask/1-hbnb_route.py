#!/usr/bin/python3
"""
This script starts a Flask web application.
The web application listens on 0.0.0.0, port 5000.
Routes:
  - /: displays "Hello HBNB!"
  - /hbnb: displays "HBNB"
Options:
  - Uses the option strict_slashes=False in route definitions.
  - Adheres to PEP 8 style (version 1.7).
"""

from flask import Flask

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

if __name__ == '__main__':
    # Run the application on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
