from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm
import time

@app.route('/')
@app.route('/index')
def index():
    #dummy user
    user= {'username': 'miguel'}
    
    # dummy post
    post = [
        {
            "author":{'username': 'henry'},
            "body":" beautiful day!! "
        },
        {
            "author":{'username': 'ford'},
            "body":" you only know what you work on!! "
        }

    ]
    return render_template("index.html", title="home", user= user, posts= post)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash(f"login from user { form.username.data}, remember me: { form.remember_me.data} ")
        time.sleep(5)
        return redirect("/login")

    return render_template("login.html", title="login", form=form)