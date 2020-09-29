import pymysql 

def insert_drink_sql():
    print("Starting SQL")
    connection = pymysql.connect(host="localhost", port=33066, user="root", password="password", database="brewapp")
    cursor = connection.cursor()

    args = (1, "Water", 0.80)
    print("Taking in args...")
    cursor.execute("INSERT into Drinks (DrinkID, Drink, Price) VALUES (%s, %s, %s)", args)
    print("Executed")
    connection.commit()
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    for row in rows:
        print(row)
    
    print("rows")
    return

insert_drink_sql()