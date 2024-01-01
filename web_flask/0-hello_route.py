#!/usr/bin/python3
""" falsk app """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """return hello hbnb"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
