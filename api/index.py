# This is just the server to host the site. basically nothing cool is here.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

