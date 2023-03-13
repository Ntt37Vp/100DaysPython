from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>INDEX</h1><br><a href="/login">Login<a>'


@app.route('/login')
def login():
    return 'LOGIN<br><a href="/hello">Hello<a>'


@app.route('/hello')
def hello():
    return 'HELLO WORLD!<br><a href="/">Back to Index<a>'




if __name__ == "__main__":
    app.run()
