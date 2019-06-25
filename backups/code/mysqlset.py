import mysql.connector


def get_mysql_connection():
    return mysql.connector.connect(user='root', password='password', database='dumps', host='host')


def run_mysql_query(query, parameters=()):
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    connection.commit()
    connection.close()
