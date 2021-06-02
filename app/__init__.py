from flask import Flask
# from .config import DevConfig
from .config import config_options 
from flask_bootstrap import Bootstrap


# Initializing flask application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(config_options['development'])
# app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import error
from app import views

# Initializing Flask Extensions
bootstrap = Bootstrap(app)