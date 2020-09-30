import pymysql 
from persistence.get_connection import connection

def insert_people_sql():
    print("Starting SQL")
    cursor = connection.cursor()

    args = (3, "Levi")
    print("Taking in args...")
    cursor.execute("INSERT into People (ID, Name) VALUES (%s, %s)", args)
    print("Executed")
    connection.commit()
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    for row in rows:
        print(row)
    
    print("rows")
    return

insert_people_sql()