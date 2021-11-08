import mysql.connector 
#import re
#from passlib.hash import bcrypt
import connection
import DBfuncs


#checks to see if the user is alredy registered in the database //works
def userExists(username):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "SELECT * FROM users WHERE userID= %s"
    my_cursor.execute(sql, (username,))
    results = my_cursor.fetchone()
    if results != None:
        return True
    else:
        return False

#returns the user enter's record //works
def getUser(username):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    q = "SELECT * FROM users WHERE userID = %s"
    my_cursor.execute(q,(username,))
    results = my_cursor.fetchone()
    return results


def passwordCheck(username, password):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "SELECT password FROM users WHERE username= %s"
    my_cursor.execute(sql, (username,))
    results = my_cursor.fetchone()
    # if (bcrypt.verify(password, results[0])) == True:
    if (password == results[0]):
        print("login granted")
        return True
    else:
        print("login failed")
        return False

#Checks the user's username and password with the one in the database and returns true or false
def login():
    username = input("Username: ")

    while(userExists(username) == False):
        username = input("That user name does not exist try again Username: ")

    password = input("Password: ")
    while(passwordCheck(username,password) != True):
        password = input("Invalid password try again. Password: ")

    return DBfuncs.getRole(username)




#Function allows a admin to delete any user //done
def deleteUser(admin):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    if admin == (1,):
        sql = "DELETE FROM user WHERE userID = %s"
        user = (input("Enter userId you wish to delete: "),)
        my_cursor.execute(sql, user)
        universitydb.commit()
        print("User deleted")
        my_cursor.close()

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

'''
#Hashes and returns a password
def passHash(password):
    hashed_password = bcrypt.hash(password)
    return hashed_password
'''

#checks to see if the user is alredy registered in the database
def userExists(username):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "SELECT * FROM users WHERE username=%s"
    my_cursor.execute(sql, (username,))
    results = my_cursor.fetchone()
    if results != None:
        return True

    else:
        return False

def add(username, password):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sqlStuff = "INSERT INTO users (username, password, role) VALUES (%s,%s,0)"
    my_cursor.execute(sqlStuff, (username, password))
    universitydb.commit()
    my_cursor.close()

#checks to see if the userID is taken and adds the user if the user does not exist.
def signUp():
    #first prompt
    userName = input("What would you like your user name to be?")
    while(userExists(userName)):
        userName = input("That user name is taken. What would you like your user name to be?")

    password = input("password:")
    password2 = input("password:")

    while(password != password2):
        print("Those passwords did not match try again")
        password = input("password:")
        password2 = input("password:")

    #if password == password2 and passwordChecker(password): password hashing later
    if(password == password2):
        if add(userName, password):
            print("User was successfully added to the database")
            return True
        else:
            print("Failed to add user")
            return False
    #else:
        #print("Passwords don't match")
        #return False
