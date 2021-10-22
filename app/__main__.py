from flask import Flask, render_template
from db import Database
import os

class RecipeBuddy(object):

    app = None
    db = None

    def __init__(self):
    
        self.start()
    
    def start(self):
        
        # Database connect
        self.db = Database(os.getenv('MARIADB_HOST'), int(os.getenv('MARIADB_PORT')), os.getenv('MARIADB_USER'), os.getenv('MARIADB_PASSWORD'), os.getenv('MARIADB_DATABASE'))
        self.db.connect()
        # Flask
        self.app = Flask(__name__)
        
        @self.app.route('/')
        def index():
            return render_template('index.html', os=os)
        
        self.app.run(host='0.0.0.0', port=5000)

RecipeBuddy()
