from .blueprints import ALL_BLUEPRINTS
from .models import db
from flask import Flask
import os


import sys
# Remove later!
try:
    from .testing import drop_db_tables, create_db_tables, create_db_test_data
except Exception as e:
    print(e, file=sys.stderr)
    exit(1)


def create_app():

    app = Flask(__name__)

    # Sign into our MariaDB database
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

    # Load all blueprints into our app
    for blueprint in ALL_BLUEPRINTS:

        app.register_blueprint(blueprint)

    # Initialize our database
    db.init_app(app)

    # Comment / uncomment the following line to delete the SQL tables we are
    # testing
    drop_db_tables(app, db)
    # Comment / uncomment the following line to create SQL database tables from
    # scratch when we run Recipe Buddy
    create_db_tables(app, db)
    # Comment / uncomment the following line to create test data in our SQL
    # database
    create_db_test_data(app, db)

    return app
