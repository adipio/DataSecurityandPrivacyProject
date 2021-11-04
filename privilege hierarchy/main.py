import mysql.connector

def fpdatabase():
    try:
        results = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1234",
        database = "universitydb",)
        return results
    except:
        print("Something went wrong with connecting to the database. \n Try checking if the SQL server is running, and check if you have the correct password in backend/connection.py")


#Adds a user to the user data base ant then returns true if they were added correctly
def addFaculty(firstName, lastName, email, job):
    universitydb = connection.universitydb()
    my_cursor = fpdatabase.cursor()
    sqlStuff = "INSERT INTO faculty (firstName, lastName, email, JOB) VALUES (%s,%s,%s,%s)"
    my_cursor.execute(sqlStuff, (firstName, lastName, email, job))
    fpdatabase.commit()
    my_cursor.close()

def addCourse(className, professorName, studentList, roomNumber, classID, creditHours, roomCapacity, numStudents, syllabus):
    universitydb = connection.universitydb()
    my_cursor = fpdatabase.cursor()
    sqlStuff = "INSERT INTO courses (className, professorName, studentList, roomNumber, classID, creditHours, roomCapacity, numStudents, syllabus) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    my_cursor.execute(sqlStuff, (className, professorName, studentList, roomNumber, classID, creditHours, roomCapacity, numStudents, syllabus))
    fpdatabase.commit()
    my_cursor.close()

def addStudent(firstName, lastName, studentID, creditHours, year, age, Advisor):
    universitydb = connection.universitydb()
    my_cursor = fpdatabase.cursor()
    sqlStuff = "INSERT INTO students (firstName, lastName, studentID, creditHours, year, age, Advisor) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    my_cursor.execute(sqlStuff, (firstName, lastName, studentID, creditHours, year, age, Advisor))
    fpdatabase.commit()
    my_cursor.close()

def deleteUser(admin): # what do we wanna delete by on each table?
    fpdatabase = connection.fpdatabase()
    my_cursor = fpdatabase.cursor()
    sql = "DELETE FROM user WHERE userID = %s"
    user = (input("Enter userId you wish to delete: "),)
    my_cursor.execute(sql, user)
    fpdatabase.commit()
    print("User deleted")
    my_cursor.close()

'__main__'

