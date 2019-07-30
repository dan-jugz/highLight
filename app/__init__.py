from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#initialising app
app =Flask(__name__,instance_relative_config=True)

#Setting up the configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Intiliazing Flask extensions
bootstrap=Bootstrap(app)

from app import views
from app import errors