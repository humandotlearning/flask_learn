from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user= {'username': 'miguel'}
    return render_template("index.html", title="home" , user= user)