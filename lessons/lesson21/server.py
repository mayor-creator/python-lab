import random
from datetime import datetime

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    random_number = random.randint(1, 10)
    date = datetime.now()
    current_year = date.year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/user/<username>")
def profile(username):
    NAME_API_ENDPOINT = "https://api.agify.io"
    name_params = {"name": username}
    response = requests.get(NAME_API_ENDPOINT, params=name_params)
    name_data = response.json()
    person_name = name_data.get("name")

    GENDER_API_ENDPOINT = "https://api.genderize.io"
    gender_params = {"name": username}
    gender_response = requests.get(GENDER_API_ENDPOINT, params=gender_params)
    gender_data = gender_response.json()

    return render_template(
        "profile.html",
        profile_name=person_name,
        profile_gender=gender_data.get("gender"),
        profile_age=name_data.get("age"),
    )


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = " https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
