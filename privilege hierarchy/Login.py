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

#Function That allows an admin to delete any post //done
def deletePost(admin):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    if admin == (1,):
        sql = "DELETE FROM post WHERE postID = %s"
        post = (input("Enter postId you wish to delete: "),)
        my_cursor.execute(sql, post)
        universitydb.commit()
        print("post deleted")
        my_cursor.close()

#Function to allow users to delete their own posts if wanted. works but may need rework due to the user needing to know the id of the post //works
def deleteSelfPost(postID, username):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "DELETE FROM post WHERE postID = %s AND postUser = %s"
    my_cursor.execute(sql, (postID, username,))
    universitydb.commit()
    my_cursor.close()

#Function to get a user's first name last name and profile pic //done
def getUserInfo(username):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "SELECT firstName, lastName, profilePicture FROM user WHERE userID = %s"
    my_cursor.execute(sql, (username,))
    results = my_cursor.fetchone()
    my_cursor.close()
    return results

#passes a user and a profile picture and sets the new profile picture
def changeProfilePic(username, newPick):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    update = "UPDATE user SET profilePicture = %s WHERE userID = %s"
    my_cursor.execute(update, (newPick, username,))
    universitydb.commit()

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
        if DBfuncs.addUser(userName, password):
            print("User was successfully added to the database")
            return True
        else:
            print("Failed to add user")
            return False
    #else:
        #print("Passwords don't match")
        #return False
