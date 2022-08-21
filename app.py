from flask import Flask
import random

from data import jokes

app = Flask(__name__)

@app.get("/")
def hello_world():
    joke = random.choice(jokes)
    return joke