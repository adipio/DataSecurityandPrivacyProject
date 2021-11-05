import mysql.connector 
from passlib.hash import bcrypt
import connection

#checks to see if the user is alredy registered in the database //works
def userExists(username):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "SELECT * FROM user WHERE userID= %s"
    my_cursor.execute(sql, (username,))
    results = my_cursor.fetchone()
    if results != None:
        return True
    else:
        return False

#Function that returns the current bio // works


#Allows user to change thier bio in the user database and returns true if it was changed false if unchanged //works
def updateBio(username, newBio):
    universitydb = connection.universitydb()
    bio = currentBio(username)
    my_cursor = universitydb.cursor()
    update = "UPDATE user SET bio = %s WHERE userID = %s"
    my_cursor.execute(update, (newBio, username,))
    universitydb.commit()
    bio3 = currentBio(username)
    if bio == bio3:
        print("not changed")
        return False
    else:
        print("bio changed")
        return True


#creates a post into the post database and returns the postID
def createPost(image, description, username, imageName):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    post = "INSERT INTO post (image, description, postUser, imageName) VALUES (%s,%s,%s, %s)"
    my_cursor.execute(post, (image, description, username, imageName,))
    universitydb.commit()
    my_cursor.close()

def getMostRecentPostId():
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    my_cursor.execute("SELECT postID from post order by createdAt desc")
    result = my_cursor.fetchone()
    return result


#creates a event into the event database // works
def createEvent(username):
    universitydb = connection.universitydb()
    eventName = input("Please enter a event name")
    description = input("Please enter a description: ")
    date = input("Please enter a date: ")
    location = input("Please enter a location: ")
    my_cursor = universitydb.cursor()
    post = "INSERT INTO event (eventName,description, location, eventUser) VALUES (%s,%s,%s,%s)"
    my_cursor.execute(post, (eventName, description, location, username,))
    universitydb.commit()
    my_cursor.close()

#function that returns  1 or zero depending on if they are a admin or not may need to change this //works
def getRole(username):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    q = "SELECT role FROM user WHERE username = %s"
    my_cursor.execute(q, (username,))
    results = my_cursor.fetchone()
    print(results)
    return results

#joins both the user and the posts table //done
#this almost fulfills the requirments
def viewPosts(username=""):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    if username == "": # this is the case that we want all posts from all users, and in that case we just want first, last, profile pic
        my_cursor.execute("SELECT postID, image, description, firstName, lastName, profilePicture, imageName from post JOIN user on userID = postUser order by createdAt desc") # this needs to be a join "Select "
        results = my_cursor.fetchall()
        return results
    else: # this is the case where we want JUST the posts from this one user, and we want that joined with first, last, profile pic, and bio ( this is inefficient unfortunately )
        q = "SELECT postID, image, description, firstName, lastName, profilePicture, imageName, bio from post right join user ON userID = %s WHERE userID = postUser order by createdAt desc" # this needs to only get the posts from username (the parameter)
        my_cursor.execute(q, (username,))
        results = my_cursor.fetchall()
        return results

#returns tuples of all the events //works
def viewEvents():
    universitydb= connection.universitydb()
    my_cursor = universitydb.cursor()
    my_cursor.execute("SELECT * FROM event")
    results = my_cursor.fetchall()
    return results

#returns the user enter's record //works
def getUser(username):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    q = "SELECT * FROM user WHERE userID = %s"
    my_cursor.execute(q,(username,))
    results = my_cursor.fetchone()
    return results


#Checks the user's username and password with the one in the database and returns true or false
def login():
    username = input("Username: ")
    password = input("Password: ")
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "SELECT password FROM user WHERE userID = %s" 
    my_cursor.execute(sql, (username,))
    results = my_cursor.fetchone()
    if (bcrypt.verify(password, results[0])) == True:
        print("login sucsess")
        return True
    else:
        print("login failed")
        return False


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


