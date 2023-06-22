import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Terigbade@1'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE tms_db")

print ("All done")