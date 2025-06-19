from flask import Flask, render_template, request
import requests
from smtplib import SMTP

MY_EMAIL = "kojozpythontesting@gmail.com"
MY_PASSWORD = "password"

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        message_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

        with SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="email",
                msg=f"Subject: New Message\n\n{message_body}"
            )

        print(f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
        return render_template("contact.html", request_m=request.method)
    else:
        return render_template("contact.html", request_m=request.method)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
