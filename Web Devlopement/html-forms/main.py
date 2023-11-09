from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def recieve_login_data():
    return "SUCCESS"


if __name__ == "__main__":
    app.run(debug=True)
