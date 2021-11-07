import connection

def addUser(username, password):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sqlStuff = "INSERT INTO users (username, password, role) VALUES (%s,%s,0)"
    my_cursor.execute(sqlStuff, (username, password))
    universitydb.commit()
    my_cursor.close()
    return True

def changeRole(username, role):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "UPDATE users SET role = %s WHERE username = %s"
    my_cursor.execute(sql, (username,role))
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
    sql = "SELECT role FROM users WHERE username=%s"
    my_cursor.execute(sql, (username,))
    results = my_cursor.fetchone()
    return results[0]

def enrollStudent(studentID,classID):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "INSERT INTO enrollments (Student,Course) VALUES (%s,%s)"
    my_cursor.execute(sql, (studentID,classID))
    universitydb.commit()
    my_cursor.close()

def viewCoursesIn(studentID):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "SELECT courses.classID, courses.className from courses join enrollments ON courses.classID = enrollments.Course where enrollments.Student = %s"
    my_cursor.execute(sql, (studentID,))
    results = my_cursor.fetchall()
    for row in results:
        print (row[0],row[1])

def viewStudentsIn(classID):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "SELECT students.studentID from students join enrollments ON students.studentID = enrollments.Student where enrollments.Course = %s"
    my_cursor.execute(sql, (classID,))
    results = my_cursor.fetchall()
    for row in results:
        print (row[0])
    