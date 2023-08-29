from flask import Flask
from random import randint


app = Flask(__name__)


def choose_num():
    return randint(1, 9)


@app.route("/")
def home_page():
    return "<h1> guess higher or lower</h1>"


right_sol = choose_num()


@app.route("/<int:userchoice>")
def choice_page(userchoice):
    if userchoice == right_sol:
        return "<h1> your right </h1>"
    else:
        if userchoice > right_sol:
            return "choose lower"
        else:
            return "choose higher"


if __name__ == "__main__":
    app.run()
