import os
from flask import Flask, render_template
from classes.database import database

app = Flask(__name__)

# Database connect
db = database(os.getenv('MARIADB_HOST'), int(os.getenv('MARIADB_PORT')), os.getenv('MARIADB_USER'), os.getenv('MARIADB_PASSWORD'), os.getenv('MARIADB_DATABASE'))
db.connect()


@app.route('/')
def index():
    return render_template('index.html', os=os)


app.run(host='0.0.0.0', port=5000)
