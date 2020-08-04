from flask import render_template
# import the app object from the ./application/__init__.py
from application import app
# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
 return render_template('home.html', title='Home')


@app.route('/add')
def add():
 return render_template('add.html', title='Calorie Count')
