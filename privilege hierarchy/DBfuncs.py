import connection

def addUser():
    username = input("Input a username to add: ")
    password = input("Input a password for a user: ")
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sqlStuff = "INSERT INTO users (username, password, role) VALUES (%s,%s,0)"
    my_cursor.execute(sqlStuff, (username, password))
    universitydb.commit()
    my_cursor.close()
    return True

def changeRole(): #this does not work
    username = input("Enter a username to change the role of: ")
    role = input("What role would you like to assign to the user? [Dean], [Advisor], [Professor]")
    roleNum = "0"
    if(role == "Dean"):
        print("role number 3")
        roleNum = "3"
    elif(role == "Advisor"):
        print("role number 2")
        roleNum = "2"
    elif(role == "Professor"):
        print("role number 1")
        roleNum = "1"
    else:
        print("Invlaid role try again")

    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "UPDATE users SET role = %s WHERE username = %s"
    my_cursor.execute(sql, (roleNum,username))
    
    universitydb.commit()
    my_cursor.close()

#Adds a user to the user data base ant then returns true if they were added correctly
def addFaculty():
    firstName = input("Enter the faculty member's  first name: ")
    lastName = input("Enter the Faculty member's last name: ")
    email = input("Enter the faculty member's email: ")
    job = input("enter the faculty member's job: ")
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sqlStuff = "INSERT INTO faculty (firstName, lastName, email, JOB) VALUES (%s,%s,%s,%s)"
    my_cursor.execute(sqlStuff, (firstName, lastName, email, job))
    universitydb.commit()
    my_cursor.close()

def addCourse():
    className = input("Enter the class name: ")
    professorName = input("Enter the professor's name: ")
    roomNumber = input("Enter the class room number: ")
    classID = input("Enter the class ID number: ")
    creditHours = input("Enter the creditHours: ")
    roomCapacity = input("Enter the room capacity: ")
    numStudents = input("Enter the number of students: ")
    syllabus = input("Add syllabus: ")
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sqlStuff = "INSERT INTO courses (className, professorName, roomNumber, creditHours, roomCapacity, numStudents, syllabus) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    my_cursor.execute(sqlStuff, (className, professorName, roomNumber, creditHours, roomCapacity, numStudents, syllabus))
    universitydb.commit()
    my_cursor.close()

def addStudent(): #works
    firstName = input("Enter the student's first name: ")
    lastName = input("Enter the student's last name: ")
    studentID = input("Enter the student's ID number: ")
    creditHours = input("Enter the credit hours: ")
    year = input("What is the year: ")
    age = input("Enter the student's age: ")
    Advisor = input("What is the student's advisor: ")
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sqlStuff = "INSERT INTO students (firstName, lastName, creditHours, year, age, Advisor) VALUES (%s,%s,%s,%s,%s,%s)"
    my_cursor.execute(sqlStuff, (firstName, lastName, creditHours, year, age, Advisor))
    universitydb.commit()
    my_cursor.close()

def deleteUser():
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "DELETE FROM users WHERE userID= %s"
    user = (input("Enter user ID you wish to delete: "),)
    my_cursor.execute(sql, user)
    universitydb.commit()
    my_cursor.close()

def deleteFaculty():
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "DELETE FROM faculty WHERE facultyID = %s"
    faculty = (input("Enter facultyID you wish to delete: "),)
    my_cursor.execute(sql, faculty)
    universitydb.commit()
    my_cursor.close()

def deleteCourse(): # what do we wanna delete by on each table?
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "DELETE FROM courses WHERE classID = %s"
    classid = (input("Enter classId you wish to delete: "),)
    my_cursor.execute(sql, classid)
    universitydb.commit()

    my_cursor.close()

def deleteStudent(): # what do we wanna delete by on each table?
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "DELETE FROM students WHERE studentID = %s"
    student = (input("Enter studentId you wish to delete: "),)
    my_cursor.execute(sql, student)
    universitydb.commit()
    print("Student deleted")
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
        print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

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
    sql = "SELECT students.studentID, students.lastName from students join enrollments ON students.studentID = enrollments.Student where enrollments.Course = %s"
    my_cursor.execute(sql, (classID,))
    results = my_cursor.fetchall()
    for row in results:
        print (row[0])
    