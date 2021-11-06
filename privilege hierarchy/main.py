import connection
import Signup

def addUser(username, password, role):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sqlStuff = "INSERT INTO users (username, password, role) VALUES (%s,%s,%s)"
    my_cursor.execute(sqlStuff, (username, password, role))
    universitydb.commit()
    my_cursor.close()

#Adds a user to the user data base ant then returns true if they were added correctly
def addFaculty(firstName, lastName, email, job):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sqlStuff = "INSERT INTO faculty (firstName, lastName, email, JOB) VALUES (%s,%s,%s,%s)"
    my_cursor.execute(sqlStuff, (firstName, lastName, email, job))
    universitydb.commit()
    my_cursor.close()

def addCourse(className, professorName, studentList, roomNumber, classID, creditHours, roomCapacity, numStudents, syllabus):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sqlStuff = "INSERT INTO courses (className, professorName, studentList, roomNumber, classID, creditHours, roomCapacity, numStudents, syllabus) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    my_cursor.execute(sqlStuff, (className, professorName, studentList, roomNumber, classID, creditHours, roomCapacity, numStudents, syllabus))
    universitydb.commit()
    my_cursor.close()

def addStudent(firstName, lastName, studentID, creditHours, year, age, Advisor):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sqlStuff = "INSERT INTO students (firstName, lastName, studentID, creditHours, year, age, Advisor) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    my_cursor.execute(sqlStuff, (firstName, lastName, studentID, creditHours, year, age, Advisor))
    universitydb.commit()
    my_cursor.close()

def deleteFaculty(): # what do we wanna delete by on each table?
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "DELETE FROM faculty WHERE userID = %s"
    user = (input("Enter userId you wish to delete: "),)
    my_cursor.execute(sql, user)
    universitydb.commit()
    print("Faculty deleted")
    my_cursor.close()

def deleteCourse(): # what do we wanna delete by on each table?
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "DELETE FROM courses WHERE userID = %s"
    user = (input("Enter userId you wish to delete: "),)
    my_cursor.execute(sql, user)
    universitydb.commit()
    print("Course deleted")
    my_cursor.close()

def deleteStudent(): # what do we wanna delete by on each table?
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "DELETE FROM students WHERE userID = %s"
    user = (input("Enter userId you wish to delete: "),)
    my_cursor.execute(sql, user)
    universitydb.commit()
    print("Course deleted")
    my_cursor.close()

def viewFaculty():
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    my_cursor.execute("SELECT * FROM faculty")
    results = my_cursor.fetchall()
    for row in results:
        print(row[0] , row[1], row[2], row[3], row[4])

def viewCourses():
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    my_cursor.execute("SELECT * FROM courses")
    results = my_cursor.fetchall()
    for row in results:
        print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

def viewStudents():
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    my_cursor.execute("SELECT * FROM students")
    results = my_cursor.fetchall()
    for row in results:
        print(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

def getRole(username):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "SELECT role FROM users WHERE username = %s"
    my_cursor.execute(sql, username)
    results = my_cursor.fetchall()
    return results

if __name__ == "__main__":

    viewFaculty()
    #viewCourses()
    #viewStudents()

    #Signup.userExists("Antonio")
    addFaculty("Ant", "D", "adipio_stu@kent.edu", "code")  # works

    addUser("Antonio", "1234", 4)
    userType = input("Are you a new user or a returning user? [N/R]")

    if(userType == "R"):
        Signup.login()
    else:
        Signup.signUp()

    addUser("Antonio", "1234", 4)
    addFaculty("Ant", "D", "adipio_stu@kent.edu", "code") #works
    addCourse("className", "professorName", "studentList", 1, 13, 16, 32, "numStudents", "syllabus") #works
    addStudent("firstName", "lastName", 1, 16, 2021, 23, "Eddy") #works