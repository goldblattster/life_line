from lifeline import app
from flask import render_template
from datetime import date

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/register/')
def register():
    return render_template('register.html', current_year=date.today().year)