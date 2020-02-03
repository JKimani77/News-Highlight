from flask import Flask
from .config import DevConfig

# to init the  app
app = Flask(__name__)

#to setup the configuration
app.config.from_object(DevConfig)

from app import views