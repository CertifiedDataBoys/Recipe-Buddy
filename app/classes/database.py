# Module Imports
import mariadb
import sys


class database:
    def __init__(database, host, port, user, password, database_name):
        database.host = host
        database.port = port
        database.user = user
        database.password = password
        database.database_name = database_name

    def connect(database):
        try:
            conn = mariadb.connect(
                user=database.user,
                password=database.password,
                host=database.host,
                port=database.port,
                database=database.database_name
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
        return conn.cursor()
