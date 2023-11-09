from flask import Flask


def make_bold(func):
    def wrapper(*args, **kwargs):
        sol = func()
        return f"<b> {sol}</b>"

    return wrapper


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello,world</h1> <p> this is a paragraph testing </p>  "


@app.route("/bye")
@make_bold
def bye():
    return "bye"


@app.route("/<name>")
def greet(name):
    return f"hello {name}"


if __name__ == "__main__":
    app.run()
