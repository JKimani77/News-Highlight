from flask import Flask
from .config import DevConfig

# to init the  app
app = Flask(__name__, instance_relative_config = True)

#to setup the configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import views


