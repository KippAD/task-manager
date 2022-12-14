# This file will make sure to initialise our taskmanager application
# and allow use to use our own imports as well as any standard.

import os
import re

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# In order to use hidden env variables we need to import the env package
if os.path.exists("env.py"):
    import env

# we are specifying two app configuration variables that will both come from
# environment variables in the env.py
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    app.config["SQLALCHEMY_DATABASE_URI"] = uri

# Create an instance of imported sqlalchemy class and set to instance of flask app
db = SQLAlchemy(app)

# declared at bottom because it relises on db and app variables
from taskmanager import routes