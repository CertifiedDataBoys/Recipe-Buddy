from flask import Flask, render_template
from db import Database
import os


app = Flask(__name__)

@self.app.route('/')
def index():
    return render_template('index.html', os=os)


if __name__ == "__main__":

    # MariaDB
    db = Database(os.getenv('MARIADB_HOST'), int(os.getenv('MARIADB_PORT')), os.getenv('MARIADB_USER'), os.getenv('MARIADB_PASSWORD'), os.getenv('MARIADB_DATABASE'))
    db.connect()
    # Flask

    self.app.run(host='0.0.0.0', port=5000)
