from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField


class LoginForm(FlaskForm):
    email = StringField('Email')
    password = StringField('Password')


app = Flask(__name__)
app.secret_key = "4fbiq$xYPXP@fELBsBJ"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
