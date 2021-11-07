import mysql.connector

def universitydb():

    try:
        results = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1234",
        database = "universitydb",)
        return results
    except:
        print("Something went wrong with connecting to the database. \n Try checking if the SQL server is running, and check if you have the correct password in backend/connection.py")
