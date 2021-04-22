from flask import Flask, Blueprint

cashman_blueprint = Blueprint("cashman_blueprint", __name__)

@cashman_blueprint.route('/')
def hello_world():
    return 'Hello world!!!!!!'
