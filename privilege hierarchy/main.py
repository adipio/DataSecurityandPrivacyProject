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
    return results

def viewCourses():
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    my_cursor.execute("SELECT * FROM courses")
    results = my_cursor.fetchall()
    return results

def viewStudents():
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    my_cursor.execute("SELECT * FROM students")
    results = my_cursor.fetchall()
    return results


'__main__'

