from flask import Flask, render_template
from post import Post
import requests


app = Flask(__name__)
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
posts_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    posts_objects.append(post_obj)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts_objects)


@app.route('/blog/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
