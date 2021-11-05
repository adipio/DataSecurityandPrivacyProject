import mysql.connector
import re
from passlib.hash import bcrypt
import connection


#checks how strong a password is returns true if it is strong
def passwordChecker(password):
    #check the password length
    if len(password) < 8:
        return False

    #checks for lower
    lowerCheck = re.compile(r'[a-z]')
    if not(lowerCheck.search(password)):
        return False

    #checks for upper
    upperCheck = re.compile(r'[A-Z]')
    if not(upperCheck.search(password)):
        return False

    #checks for number
    numCheck = re.compile(r'\d')
    if not(numCheck.search(password)):
        return False

    #checks for special character
    spCheck = re.compile(r'\W')
    if not(spCheck.search(password)):
        return False
    else:
        return True

#Hashes and returns a password
def passHash(password):
    hashed_password = bcrypt.hash(password)
    return hashed_password

#checks to see if the user is alredy registered in the database
def userExists(username):

    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "SELECT * FROM user WHERE userID= %s"

    my_cursor.execute(sql, (username,))
    results = my_cursor.fetchone()
    my_cursor.close()
    if results != None:
        return True
    else:
        return False

#Adds a user to the user data base ant then returns true if they were added correctly
def addUser(username, password):

    universitydb = connection.universitydb()
    initalCheck = userExists(username) #this may not work
    my_cursor = universitydb.cursor()
    sqlStuff = "INSERT INTO user (username, password) VALUES (%s,%s)"
    my_cursor.execute(sqlStuff, (username, passHash(password)))
    universitydb.commit()

    my_cursor.close()
    afterCheck = userExists(username)
    if initalCheck == False and afterCheck == True:
        return True
    else:
        return False

#checks to see if the userID is taken and adds the user if the user does not exist.
def signUp():
    userName = input("What would you like your user name to be?")
    password = input("password:")
    password2 = input("password:")

    if password == password2 and passwordChecker(password):
        if addUser(userName, password):
            print("User was successfully added to the database")
            return True
        else:
            print("Failed to add user")
            return False
    else:
        print("Passwords don't match")
        return False


