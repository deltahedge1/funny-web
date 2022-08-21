from flask import Flask
from flask import render_template
import random

import data

app = Flask(__name__)

@app.get("/")
def hello_world():
    joke = random.choice(data.jokes)
    return render_template('joke.html', joke_text=joke)