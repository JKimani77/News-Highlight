from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap


# to init the  app
app = Flask(__name__, instance_relative_config = True)

#to setup the configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


# Initializing Flask Extensions
bootstrap = Bootstrap(app)


from app import views
from app import errors


