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

def deleteFaculty(facultyID): # what do we wanna delete by on each table?
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "DELETE FROM faculty WHERE userID = %s"
    user = (input("Enter userId you wish to delete: "),)
    my_cursor.execute(sql, user)
    universitydb.commit()
    print("Faculty deleted")
    my_cursor.close()

def deleteCourse(courseID): # what do we wanna delete by on each table?
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sql = "DELETE FROM courses WHERE userID = %s"
    user = (input("Enter userId you wish to delete: "),)
    my_cursor.execute(sql, user)
    universitydb.commit()
    print("Course deleted")
    my_cursor.close()

def deleteStudent(studentID): # what do we wanna delete by on each table?
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
    #return results

def viewCourses():
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    my_cursor.execute("SELECT * FROM courses")
    results = my_cursor.fetchall()
    #return results

def viewStudents():
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    my_cursor.execute("SELECT * FROM students")
    results = my_cursor.fetchall()
    #return results

if __name__ == "__main__":

    userType = input("Are you a new user or a returning user? [N/R]")

    if(userType == "R"):
        Signup.login()
    else:
        Signup.signUp()


    addFaculty("Ant", "D", "adipio_stu@kent.edu", "code") #works
    addCourse("className", "professorName", "studentList", 1, 13, 16, 32, "numStudents", "syllabus") #works
    addStudent("firstName", "lastName", 1, 16, 2021, 23, "Eddy") #works

    addStudent("Dominic", "DiTirro", 810830000, 12, 2021, 24, "Max");
    addStudent("Eddy", "Brock", 80349510, 8, 2021, 29, "John");
    addStudent("Ash", "Ketchum", 837852019, 18, 2024, 12, "Eddy");
    addStudent("Peter", "Parker", 90495039, 21, 2021, 19, "Max:");
    addStudent("John", "Doe", 810562930, 0, 2025, 18, "Chris");
    addStudent("Jane", "Doe", 809389832, 0, 2025, 18, "Eddy");
    addStudent("James", "Roday", 803841239, 12, 2022, 28, "Eddy");
    addStudent("Charles", "Conway", 893849282, 14, 2022, 16, "Eddy");
    addStudent("Samantha", "Espen", 810938039, 12, 2022, 19, "John");
    addStudent("Emily", "Brown", 930281920, 16, 2021, 20, "Max");
    addStudent("Tom", "Cruise", 930485932, 19, 2023, 27, "Chris");
    addStudent("Jimmy", "Fallon", 192051231, 8, 2024, 26, "Max");
    addStudent("Thomas", "Brady", 302934012, 15, 2023, 25, "Chris");
    addStudent("Jermaine", "Cole", 829342034, 14, 2023, 28, "Max");
    addStudent("Aubrey", "Plaza", 839402934, 12, 2024, 27, "John");
    addStudent("Jenna", "Fischer", 392048193, 12, 2025, 30, "Chris");


    addFaculty("Daniel", "Craig", "dcraig@kent.edu", "Professor");
    addFaculty("Dwayne", "Johnson", "djohnso68@kent.edu", "Maintenance");
    addFaculty("Sofia", "Vergara", "svergar1@kent.edu", "Professor");
    addFaculty("Angelina", "Jolie", "ajolie@kent.edu", "Maintenance");
    addFaculty("William", "Smith", "wsmith42", "Janitor");
    addFaculty("Denzel", "washington", "dwashing@kent.edu", "Professor");
    addFaculty("Gal", "Gadot", "ggadot@kent.edu", "Professor");
    addFaculty("Emily", "Blunt", "eblunt@kent.edu", "Maintenance");
    addFaculty("Leonardo", "DiCaprio", "ldicapr@kent.edu", "Professor");
    addFaculty("Mark", "Wahlberg", "mwahlbe@kent.edu", "Janitor");
    addFaculty("Nicole", "Kidman", "nkidman@kent.edu", "Janitor");
    addFaculty("Emma", "Watson", "ewatson@kent.edu", "Admin");
    addFaculty("Ryan", "Gosling", "rgoslin@kent.edu", "Admin");
