from flask import Flask, render_template
from random import randint
import requests as r
import datetime


app = Flask(__name__)
footer_year = datetime.datetime.now().year


def get_gender(name: str) -> str:
    try:
        response = r.get(url=f"https://api.genderize.io?name={name}")
        gender = response.json()["gender"]
        return gender
    except Exception as err:
        return "Gender Server error"


def get_age(name: str) -> str:
    try:
        response = r.get(url=f"https://api.agify.io?name={name}")
        age = response.json()["age"]
        return age
    except Exception as err:
        return "age Server error"


@app.route("/")
def homepage():
    rand_num = randint(1, 10)
    return render_template("index.html", rand_num=rand_num, footer_year=footer_year)


@app.route("/guess/<name>")
def gender_age_predicter(name):
    pred_gender = get_gender(name)
    pred_age = get_age(name)
    return render_template(
        "gender_age_predictor.html",
        name=name,
        pred_gender=pred_gender,
        pred_age=pred_age,
        footer_year=footer_year,
    )


@app.route("/blogs")
def blog_posts():
    blog_data_api_url = "https://api.npoint.io/813f3bebf3a81bfda8cd"
    response = r.get(blog_data_api_url)
    all_blog_post = response.json()
    return render_template("blogs.html", blogs_data=all_blog_post)


if __name__ == "__main__":
    app.run()
