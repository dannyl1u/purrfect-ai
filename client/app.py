import os
import random

import requests

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        url = 'http://localhost:8080/translate'
        params = {'name': response.choices[0].text}

        response = requests.get(url, params=params)    
        return redirect(url_for("index", result=response.content))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest one funny animal name that is also a pun.

Animal: Cat
Names: Clawdia
Animal: Dog
Names: Chewbarka
Animal: {}
Names:""".format(
        animal.capitalize()
    )
