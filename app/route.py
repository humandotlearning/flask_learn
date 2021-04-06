from flask import render_template
from app import app

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