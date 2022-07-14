from flask import Flask, redirect, render_template, request
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///froshims.db")
    
SPORTS = [
    
    "Dodgeball",
    "Soccer",
    "Basketball",
    "Tennis",
    "Swimming"
]    
    

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

    
@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")
        
    
    return redirect("/registrants")
    
@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)