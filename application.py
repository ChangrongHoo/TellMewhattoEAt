import os
import random

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

from helpers import apology

# Configure application
app = Flask(__name__, template_folder='template')

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///food.db")

@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/go",methods=["GET"])
def go():
    return render_template("quiz.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if (request.method == "GET"):
        day = request.values.get("day")
        pocket = request.values.get("pocket")
        excepting = request.values.get("excepting")
        pizza = request.values.get("pizza")

        if not day or not pocket or not excepting or not pizza:
            return apology ("Please answer all the question!")

        food = db.execute("SELECT food FROM data WHERE price = ? AND special = ? AND type = ? AND portion = ? ORDER BY RANDOM() LIMIT 1", pocket, day, excepting, pizza)[0]["food"]
        return render_template("result.html", food = food)
    else:
        return render_template("quiz.html")

@app.route("/img",methods=["GET"])
def img():
    return render_template("stby.html")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

