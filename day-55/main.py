from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def bold():
        return f"<b>{func()}</b>"
    return bold

def make_emphasis(func):
    def emphasis():
        return f"<i>{func()}</i>"
    return emphasis

def make_underlined(func):
    def underlined():
        return f"<u>{func()}</u>"
    return underlined


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye, World!"
#
#
# @app.route("/<item>")
# def greet(item):
#     """This is my third flask app."""
#     return f"<p>Hello, {item}</p>"
#
#
# @app.route("/<item>/<int:number>")
# def greet_num(item, number):
#     """This is my fourth flask app."""
#     return f"<p>Hello, {item} and {number}</p>"


if __name__ == "__main__":
    app.run(debug=True)
