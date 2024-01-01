#!/usr/bin/python3
# a flask app
from flask import Flask

app = Flask(__name__)

# Define a route for the home page
@app.route('/', strict_slashes=False)
def home():
    return 'Hello HBNB!'

if __name__ == '__main__':
    # Run the application on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)

