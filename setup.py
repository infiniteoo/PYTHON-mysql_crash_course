import mysql.connector
from database import cursor

DB_NAME = 'acme'

TABLES = {}

TABLES['logs'] = (
    "CREATE TABLE `logs` ("
    " `id` int(11) NOT NULL AUTO_INCREMENT,"
    " `text` varchar(250) NOT NULL,"
    "  `user` varchar(250) NOT NULL,"
    "`created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Databased {} created!".format(DB_NAME))

create_database()
