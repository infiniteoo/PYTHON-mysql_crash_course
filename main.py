from re import A
from database import cursor, db

def add_log(text, user):
    sql = ("INSERT INTO logs(text, user) VALUES (%s, %s)")
    cursor.execute(sql, (text, user,))
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))

add_log('This is log one', 'Brad')
add_log('This is log two', 'Jeff')
add_log('This is log three', 'Troy')