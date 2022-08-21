from flask import Flask
from flask import render_template
import random

from data import jokes

app = Flask(__name__)

@app.get("/")
def hello_world():
    joke = random.choice(jokes)
    return render_template('joke.html', joke_text=joke)