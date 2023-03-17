from flask import Flask, render_template
import datetime
import random
import requests


app = Flask(__name__)
current_year = datetime.datetime.now().year
gender_url = "https://api.genderize.io/"
age_url = "https://api.agify.io/"


@app.route("/")
def index():
    rand_num = random.randint(1, 100)
    return render_template("index.html", num=rand_num, year=current_year)


@app.route("/guess/<username>")
def guess(username):
    gender_param = {
        "name": username
    }
    age_param = {
        "name": username
    }
    guess_gender = requests.get(gender_url, params=gender_param).json()["gender"]
    guess_age = requests.get(age_url, params=age_param).json()["age"]
    return render_template("guess.html", name=username, gender=guess_gender, age=guess_age, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
