from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Flask uses the location of the module passed here as a starting point when it needs to load associated resources such as template files
app = Flask(__name__)
app.config.from_object(Config)

# database
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# The bottom import is a workaround to circular imports,
# a common problem with Flask applications.
# You are going to see that the routes module needs to import the app variable defined in this script,
# so putting one of the reciprocal imports at the bottom avoids the error that results from the mutual references between these two files.
# models: defines the structure of the flask db
from app import route, models
