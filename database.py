import mysql.connector

config = {
    'user': 'root',
    'password': 'blahblah',
    host: 'localhost'
}


db = mysql.connector.connect(**config)

cursor = db.cursor()