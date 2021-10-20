# Module Imports
import mariadb
import sys
import os

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user=os.getenv('MARIADB_USER'),
        password=os.getenv('MARIADB_PASSWORD'),
        host=os.getenv('MARIADB_HOST'),
        port=3306,
        database=os.getenv('MARIADB_DATABASE')

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()