from random import randint
from flask import Flask

app = Flask(__name__)


# Constants
HOME = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'
HIGH = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'
LOW = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'
MATCH = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'


@app.route("/")
def index():
    return "<h1>Guess a number between 0 to 9</h1><br>" \
           f"<img src={HOME}>"


# Generate a random number between 0 and 9
rand_number = randint(0, 9)


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > rand_number:
        return f"<h1>Too HIGH</h1><img src={HIGH}>"
    elif guess < rand_number:
        return f"<h1>Too LOW!</h1><br><img src={LOW}>"
    else:
        return f"<h1>You got me!</h1><br><img src={MATCH}>"


if __name__ == "__main__":
    app.run(debug=True)
