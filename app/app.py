import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    db_host = os.environ.get('MARIADB_HOST')
    db_user = os.environ.get('MARIADB_USER')
    db_pass = os.environ.get('MARIADB_PASSWORD')
    db_db = os.environ.get('MARIADB_DATABASE')
    return render_template('index.html', os=os)

app.run(host='0.0.0.0', port=5000)
