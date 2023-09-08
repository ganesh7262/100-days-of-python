from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def indexhtml():
    return render_template("index.html")


@app.route("/welcome")
def welcome_page():
    return render_template("welcome.html")


if __name__ == "__main__":
    app.run()
