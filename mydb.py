import pymysql

# Establish a connection to the MySQL server
dataBase = pymysql.connect(
    host='localhost',
    user='root',
    password='Devanshu@123'
)

# Rest of your code remains unchanged
cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")
print("All DONE!")