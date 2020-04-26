from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "MarkyMark"}
    return render_template("index.html", title="Homey", user=user)
