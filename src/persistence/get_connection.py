import pymysql

def get_connection():
    return pymysql.connect(host="localhost", port=33066, user="root", password="password", database="brewapp")

connection = get_connection()