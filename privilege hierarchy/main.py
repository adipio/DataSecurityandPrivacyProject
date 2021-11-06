import connection
import Signup

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
    # Delete based on ID
    # Print out the ID

    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "DELETE FROM faculty WHERE facultyID = %s"
    user = (input("Enter FacultyID you wish to delete: "),)
    my_cursor.execute(sql, user)
    universitydb.commit()
    print("Faculty deleted")
    my_cursor.close()

def deleteCourse(): # what do we wanna delete by on each table?
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "DELETE FROM courses WHERE courseID = %s"
    user = (input("Enter CourseID you wish to delete: "),)
    my_cursor.execute(sql, user)
    universitydb.commit()
    print("Course deleted")
    my_cursor.close()

def deleteStudent(): # what do we wanna delete by on each table?
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "DELETE FROM students WHERE userID = %s"
    user = (input("Enter StudentID you wish to delete: "),)
    my_cursor.execute(sql, user)
    universitydb.commit()
    print("Student deleted")
    my_cursor.close()

def viewFaculty():
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    my_cursor.execute("SELECT * FROM faculty")
    results = my_cursor.fetchall()
    for row in results:
        print(row[0] , row[1], row[2], row[3])

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

if __name__ == "__main__":

    addFaculty("Ant", "D", "adipio_stu@kent.edu", "code")  # works
    viewFaculty()   # works
    deleteFaculty() # Needs testing
    viewFaculty()
    
    #viewCourses()  # works
    #viewStudents()


    userType = input("Are you a new user or a returning user? [N/R]")

    if(userType == "R"):
        Signup.login()
    else:
        Signup.signUp()


    addFaculty("Ant", "D", "adipio_stu@kent.edu", "code") #works
    addCourse("className", "professorName", "studentList", 1, 13, 16, 32, "numStudents", "syllabus") #works
    addStudent("firstName", "lastName", 1, 16, 2021, 23, "Eddy") #works