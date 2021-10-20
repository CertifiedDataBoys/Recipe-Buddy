import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
<<<<<<< HEAD
    db_host = os.environ.get('MARIADB_HOST')
    db_user = os.environ.get('MARIADB_USER')
    db_pass = os.environ.get('MARIADB_PASSWORD')
    db_db = os.environ.get('MARIADB_DATABASE')
    return '<b><i>TESTING</i></b><br>Host: ' + db_host + '<br>User: ' + db_user + '<br>Pass: ' + db_pass + '<br>Database: ' + db_db
=======
    return render_template('index.html', os=os)

>>>>>>> refs/remotes/origin/main

app.run(host='0.0.0.0', port=5000)
