##################################################################################

# defining the website paths

########################################################################################


from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    # dummy user
    user = {"username": "miguel"}

    # dummy post
    post = [
        {"author": {"username": "henry"}, "body": " beautiful day!! "},
        {"author": {"username": "ford"}, "body": " you only know what you work on!! "},
    ]
    return render_template("index.html", title="home", user=user, posts=post)


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()

    # check if form valid
    if form.validate_on_submit():
        # shows a flash message, tmeplate for which is provided inside index.html
        flash(
            f"login from user: { form.username.data}, remember me: { form.remember_me.data} "
        )

        # using url_for() instead of direct url like: '/index'
        # used because it is easier to handle urls like this and can also handle complex urls
        # redirect(): takes page to a new link
        return redirect(url_for("index"))

    return render_template("login.html", title="login", form=form)
