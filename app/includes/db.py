# Module Imports
import mariadb
import sys
import os

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user=os.environ.get('MARIADB_USER'),
        password=os.environ.get('MARIADB_PASSWORD'),
        host=os.environ.get('MARIADB_HOST'),
        port=3306,
        database=os.environ.get('MARIADB_DATABASE')

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()