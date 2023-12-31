from flask import Flask, render_template, request


app = Flask(__name__)


def validate_login(username, password) -> bool:
    return username == "ganesh" and password == "ganesh"


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def recieve_login_data():
    if request.method == "POST":
        un = request.form["username"]
        ps = request.form["password"]

        if validate_login(un, ps):
            return render_template("user_login_page.html", data=(un, ps))

    return "ERROR"


if __name__ == "__main__":
    app.run()
