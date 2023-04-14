from flask import Flask, render_template
import requests

API_Endpoint = "https://api.npoint.io/d2234472e3f912924ebc"
posts = requests.get(API_Endpoint).json()

app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# Run flask app
if __name__ == "__main__":
    app.run(debug=True)
