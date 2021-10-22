from flask import Flask, render_template
from classes.database import database
import os

class recipe_buddy:
    def __init__(self):
        self.start()
    def start(self):
        # Database connect
        db = database(os.getenv('MARIADB_HOST'), int(os.getenv('MARIADB_PORT')), os.getenv('MARIADB_USER'), os.getenv('MARIADB_PASSWORD'), os.getenv('MARIADB_DATABASE'))
        db.connect()
        # Flask
        app = Flask(__name__)
        @app.route('/')
        def index():
            return render_template('index.html', os=os)
        app.run(host='0.0.0.0', port=5000)

recipe_buddy()
