from db import Database
import os

if __name__ == "__main__":

    d = Database(os.getenv('MARIADB_HOST'), int(os.getenv('MARIADB_PORT')), os.getenv('MARIADB_USER'), os.getenv('MARIADB_PASSWORD'), os.getenv('MARIADB_DATABASE'))
    print(d)
