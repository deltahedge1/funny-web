from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

jokes = [
    "Relationship status? I'll leave that in the database",
    "What diet did the ghost developer go on? Boolean",
    "How do you get the code from a bank vault? You checkout the their branch"
]

@app.get("/")
def hello_world():
    joke = random.choice(jokes)
    return render_template('joke.html', joke_text=joke)