from flask import Flask, render_template
import requests

URL = "https://api.npoint.io/05ea919aad51741c3729"

app = Flask(__name__)


def get_blog_data():
    response = requests.get(URL)
    return response.json()


@app.route('/')
def home():
    blog_data = get_blog_data()
    return render_template("index.html", blogs=blog_data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:post_id>')
def post(post_id):
    blog_data = get_blog_data()
    requested_post = next((blog for blog in blog_data if blog["id"] == post_id), None)
    return render_template("post.html", post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)
