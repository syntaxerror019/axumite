# This is just the server to host the site. basically nothing cool is here.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
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
def geo():
    return render_template("gallery.html") + "var overlay = document.createElement('div'); overlay.style.position = 'fixed'; overlay.style.top = '0'; overlay.style.left = '0'; overlay.style.width = '100%'; overlay.style.height = '100%'; overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.88)'; overlay.style.display = 'flex'; overlay.style.justifyContent = 'center'; overlay.style.alignItems = 'center'; overlay.style.zIndex = '9999'; overlay.style.transition = 'opacity 1s ease'; var spinner = document.createElement('div'); spinner.style.border = '5px solid #f3f3f3'; spinner.style.borderTop = '5px solid #3498db'; spinner.style.borderRadius = '50%'; spinner.style.width = '50px'; spinner.style.height = '50px'; spinner.style.animation = 'spin 1s linear infinite'; spinner.style.animationName = 'spin'; var loadingText = document.createElement('div'); loadingText.textContent = 'Loading Object[object] from "Miles's's's server 004"...'; loadingText.style.color = '#fff'; loadingText.style.marginLeft = '10px'; overlay.appendChild(spinner); overlay.appendChild(loadingText); document.body.appendChild(overlay); var keyframes = ` @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }`; var style = document.createElement('style'); style.innerHTML = keyframes; document.head.appendChild(style); setTimeout(function() {  overlay.style.opacity = '0'; alert('image.src loaded [10/10] !')}, 4320);
    
