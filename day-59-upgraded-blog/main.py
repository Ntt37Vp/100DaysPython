from flask import Flask, render_template, request
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


@app.route("/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/form-entry", methods=["POST"])
def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    return f"<h1>Message sent. Thanks!</h1><br><p>{name}</p>"


# Run flask app
if __name__ == "__main__":
    app.run(debug=True)
