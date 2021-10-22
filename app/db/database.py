import mariadb
import sys

class Database(object):

    host = ""
    port = 0
    user = ""
    password = ""
    database_name = ""

    def __init__(self, host, port, user, password, database_name):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database_name = database_name

        print(self.__str__())

    def connect(self):
        try:
            conn = mariadb.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database_name
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}", file=sys.stderr)
            sys.exit(1)
            return None
        return conn.cursor()

    def __str__(self):

        return "{0.user}@{0.host}:{0.port} on DB {0.database_name}".format(self)
