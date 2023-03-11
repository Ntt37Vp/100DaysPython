from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>INDEX</h1><br><a href="/login">Login<a>'


@app.route('/hello')
def hello():
    return '<h2>HELLO WORLD!</h2><br><a href="/">Back to Index<a>'


@app.route('/login')
def login():
    return '<h2>LOGIN</h2><br><a href="/hello">Hello<a>'
