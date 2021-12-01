"""
    This is the module that represents the Recipe Buddy app.
    Flask should initialize from this file.
"""


from flask.helpers import send_from_directory
from .api import ALL_API_BLUEPRINTS
from .blueprints import ALL_BLUEPRINTS
from .errors import ALL_ERROR_HANDLERS
from .models import *
from .security.logins import login_manager
from flask import Flask
import os


# Remove later!
import sys
try:
    from .testing import (
        drop_db_tables, create_db_tables,
        delete_db_entries, create_db_test_data
    )
except Exception as e:
    print(e, file=sys.stderr)
    exit(1)


def create_app():
    """
        Create and run the Recipe Buddy app.
    """

    app = Flask(__name__)

    @app.route('/<path:path>')
    def send_public(path):
        return send_from_directory('public', path)

    @app.route('/profile-photos/<path:path>')
    def send_profile_photos(path):
        return send_from_directory('/data/profile_photos', path)

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'ALL_BLUEPRINTS': ALL_BLUEPRINTS}

    # Sign into our MariaDB database
    if os.getenv('SQLALCHEMY_DATABASE_URI') is not None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = "mariadb+mariadbconnector://{0}:{1}@{2}:{3}/{4}".format(
            os.getenv("MARIADB_USER"),
            os.getenv("MARIADB_PASSWORD"),
            os.getenv("MARIADB_HOST"),
            os.getenv("MARIADB_PORT"),
            os.getenv("MARIADB_DATABASE")
        )

    # Don't track modifications --- this will be removed from SQLAlchemy in a
    # future update
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Set our secret key
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    # Load all blueprints into our app
    for blueprint in ALL_BLUEPRINTS:

        app.register_blueprint(blueprint)

    # Load all API-related blueprints into our app
    for blueprint in ALL_API_BLUEPRINTS:

        app.register_blueprint(blueprint)

    # Load all error handlers into our app:
    for err in ALL_ERROR_HANDLERS:

        app.register_error_handler(*err)

    # Initialize our database
    db.init_app(app)

    # Comment / uncomment the following line to delete the SQL tables we are
    # testing
    # drop_db_tables(app, db)
    # Comment / uncomment the following line to create SQL database tables from
    # scratch when we run Recipe Buddy
    # create_db_tables(app, db)
    # Comment / uncomment the following line to remove test data in our SQL
    # database
    delete_db_entries(app, db)
    # Comment / uncomment the following line to create test data in our SQL
    # database
    create_db_test_data(app, db)

    # Initialize our login manager
    login_manager.init_app(app)
    login_manager.login_view = "login"

    return app
