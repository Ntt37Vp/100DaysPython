from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>HomePage</h1><br><img src='https://media.giphy.com/media/11s7Ke7jcNxCHS/giphy.gif'>"


# Using Variable <variable_name> Names
@app.route("/user/<username>")
def show_user_profile(username):
    # show the user profile of that user
    return f"Hello {username}"


# Making bold decorators
def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


@app.route("/bold")
@make_bold
def bold():
    return "Hello I am bold"



# Run the flask app
if __name__ == "__main__":
    app.run(debug=True)
