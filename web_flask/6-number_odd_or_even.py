#!/usr/bin/python3
""" url and value representaion """

from flask import Flask, render_template

app = Flask(__name__)


# Routes
@app.route('/')
def index():
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    return 'HBNB'

@app.route('/c/<text>')
def c(text):
    return 'C ' + text.replace('_', ' ')

@app.route('/python/')
@app.route('/python/<text>')
def python(text='is_cool'):
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>')
def number(n):
    return f'{n} is a number'

@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('combined_template.html', n=n, is_number_template=True)

@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    return render_template('combined_template.html', n=n, is_number_template=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
