import pymysql 

def insert_people_sql():
    print("Starting SQL")
    connection = pymysql.connect(host="localhost", port=33066, user="root", password="password", database="brewapp")
    cursor = connection.cursor()

    args = (2, "Jill")
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