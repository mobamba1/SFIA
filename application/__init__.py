# import Flask class from the flask module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv
# create a new instance of Flask and store it in app 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('MY_SECRET_KEY')
db = SQLAlchemy(app)


# import the ./application/routes.py file
from application import routes
