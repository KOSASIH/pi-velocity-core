from flask import Flask
from flask_restful import Api

from src.api import ExampleResource

def create_app():
    app = Flask(__name__)

    api = Api(app)

    api.add_resource(ExampleResource, "/example")

    return app
