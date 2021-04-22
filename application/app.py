from flask import Flask, url_for, g

from application.cashman_blueprint import cashman_blueprint


import json
import os

def create_app(config_name):

    app = Flask(__name__)

    config_module = f"application.config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)
      
    # Register Extensions 
    register_extensions(app)
    # Register Blueprints
    register_blueprints(app)

    @app.before_first_request
    def start_up():
        print("=========="*3)
        print(f"start up function")
        print("=========="*3)

    return app

def register_extensions(app):
    
    return None

def register_blueprints(app):
   
    app.register_blueprint(cashman_blueprint)
    
    return None
