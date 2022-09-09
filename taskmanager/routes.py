from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task


# Creating a view that renders base.html every time the user is in main route
@app.route("/")
def home():
    return render_template("base.html")
