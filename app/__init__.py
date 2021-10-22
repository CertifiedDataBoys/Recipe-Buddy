from .blueprints import ALL_BLUEPRINTS
from .db import Database
from flask import Flask

def create_app():

    app = Flask(__name__)

    for blueprint in ALL_BLUEPRINTS:

        app.register_blueprint(blueprint)

    return app
