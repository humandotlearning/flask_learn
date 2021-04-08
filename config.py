import os

base_pth = os.path.abspath( os.path.dirname(__file__))
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or "you-will-never-guess"

    # database
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
            'sqlite:///' + os.path.join(base_pth, 'app.db')

    # feature of Flask-SQLAlchemy that I do not need, which is to signal the application every time a change is about to be made in the database.
    SQLALCHEMY_TRACK_MODIFICATIONS = False