# This is just the server to host the site. basically nothing cool is here.
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/<url>')
def home(url):
    if url is not None:
        return redirect("https://github.com/syntaxerror019/axumite")
    return render_template("index.html")

@app.route('/economy')
def econ():
    return render_template("economy.html")

@app.route('/trade')
def trad():
    return render_template("trade.html")

@app.route('/geography')
def geo():
    return render_template("geo.html")

@app.route('/gallery')
def gallery_skjdhfl():
    return render_template("gallery.html")
