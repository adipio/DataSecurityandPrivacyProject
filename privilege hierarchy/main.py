import connection
import Login
import DBfuncs
'''
def admin():
    #everything

def dean():
    #can add and delete professors and advisors

def advisor():
    #add or remove students from courses, change students program

def Professor():
    #change the course title and syllabus

def Student():
    #only able to view courses

'''

def add(username, password):
    universitydb = connection.universitydb()
    my_cursor = universitydb.cursor()
    sqlStuff = "INSERT INTO users (username, password, role) VALUES (%s,%s,0)"
    my_cursor.execute(sqlStuff, (username, password))
    universitydb.commit()
    my_cursor.close()

if __name__ == "__main__":

    #viewFaculty()

    #viewCourses()
    #viewStudents()

    #DBfuncs.getRole("Antonio")

    #Signup.userExists("Antonio")
    #DBfuncs.addFaculty("Ant", "D", "adipio_stu@kent.edu", "code")  # works

    #DBfuncs.addUser("Antonio", "1234")
    userType = input("Are you a new user or a returning user? [N/R]")



    if(userType == "R"):
        userRole = Login.login()

        match userRole:
            case 4:
                print("Admin")
                print("What would you like to do [addUser], [addFaculty], [addCourse], [addStudent], [deleteCourse], [deleteStudent], [viewFaculty]")
                print("[viewUsers],[viewCourses], [viewStudents], [changeRole], [enrollStudent], [coursesIn], [studentsIn]")
                command = input("Selection:")
                if(command == "addUser"):
                    DBfuncs.addUser()
                elif(command == "addFaculty"):
                    DBfuncs.addFaculty()
                elif(command == "addCourse"):
                    DBfuncs.addCourse()
                elif(command == "addStudent"):
                    DBfuncs.addStudent()
                elif(command == "deleteUser"):
                    DBfuncs.deleteUser()
                elif(command == "deleteFaculty"):
                    DBfuncs.deleteFaculty()
                elif(command == "deleteCourse"):
                    DBfuncs.deleteCourse()
                elif(command == "deleteStudent"):
                    DBfuncs.deleteStudent()
                elif (command == "viewFaculty"):
                    DBfuncs.viewFaculty()
                elif (command == "viewUsers"):
                    DBfuncs.viewUsers()
                elif (command == "viewCourses"):
                    DBfuncs.viewCourses()
                elif (command == "viewStudents"):
                    DBfuncs.viewStudents()
                elif(command == "changeRole"):
                    DBfuncs.changeRole()
                elif(command == "enrollStudent"):
                    studentid = input("Enter student id:")
                    courseid = input("Enter course id:")
                    DBfuncs.enrollStudent(studentid,courseid)
                elif(command == "coursesIn"):
                    studentid = input("Enter student id:")
                    DBfuncs.viewCoursesIn(studentid)
                elif(command == "studentsIn"):
                    courseid = input("Enter course id:")
                    DBfuncs.viewStudentsIn(courseid)
                else:
                    print("invalid input")
            case 3:
                print("Dean")
                print("What would you like to do [addFaculty], [addCourse], [addStudent], [deleteCourse], [deleteStudent], [viewFaculty]")
                print("[viewCourses], [viewStudents], [enrollStudent], [coursesIn], [studentsIn]")
                command = input("Selection:")
                if(command == "addFaculty"):
                    DBfuncs.addFaculty()
                elif(command == "addCourse"):
                    DBfuncs.addCourse()
                elif(command == "addStudent"):
                    DBfuncs.addStudent()
                elif(command == "deleteCourse"):
                    DBfuncs.deleteCourse()
                elif(command == "deleteStudent"):
                    DBfuncs.deleteStudent()
                elif(command == "viewFaculty"):
                    DBfuncs.viewFaculty()
                elif(command == "viewCourses"):
                    DBfuncs.viewCourses()
                elif(command == "viewStudents"):
                    DBfuncs.viewStudents()
                elif(command == "enrollStudent"):
                    studentid = input("Enter student id:")
                    courseid = input("Enter course id:")
                    DBfuncs.enrollStudent(studentid,courseid)
                elif(command == "coursesIn"):
                    studentid = input("Enter student id:")
                    DBfuncs.viewCoursesIn(studentid)
                elif(command == "studentsIn"):
                    courseid = input("Enter course id:")
                    DBfuncs.viewStudentsIn(courseid)
            case 2:
                print("Advisor")
                print("What would you like to do [viewFaculty], [viewCourses], [viewStudents], [enrollStudent], [coursesIn], [studentsIn]")
                command = input("Selection:")
                if(command == "viewFaculty"):
                    DBfuncs.viewFaculty()
                elif(command == "viewCourses"):
                    DBfuncs.viewCourses()
                elif(command == "viewStudents"):
                    DBfuncs.viewStudents()
                elif(command == "enrollStudent"):
                    studentid = input("Enter student id:")
                    courseid = input("Enter course id:")
                    DBfuncs.enrollStudent(studentid,courseid)
                elif(command == "coursesIn"):
                    studentid = input("Enter student id:")
                    DBfuncs.viewCoursesIn(studentid)
                elif(command == "studentsIn"):
                    courseid = input("Enter course id:")
                    DBfuncs.viewStudentsIn(courseid)
            case 1:
                print("Professor")
                print("What would you like to do [viewFaculty], [viewCourses], [viewStudents], [studentsIn]")
                command = input("Selection:")
                if(command == "viewFaculty"):
                    DBfuncs.viewFaculty()
                elif(command == "viewCourses"):
                    DBfuncs.viewCourses()
                elif(command == "viewStudents"):
                    DBfuncs.viewStudents()
                elif(command == "studentsIn"):
                    courseid = input("Enter course id:")
                    DBfuncs.viewStudentsIn(courseid)
            case 0:
                print("Student")
                print("What would you like to do [viewCourses], [viewStudents]")
                command = input("Selection:")
                if(command == "viewFaculty"):
                    DBfuncs.viewFaculty()
                elif(command == "viewCourses"):
                    DBfuncs.viewCourses()
                elif(command == "viewStudents"):
                    DBfuncs.viewStudents()
                elif(command == "studentsIn"):
                    courseid = input("Enter course id:")
                    DBfuncs.viewStudentsIn(courseid)

        '''
        if(userRole == 4):
            print("Admin")
        elif(userRole == 3):
            print("Dean")
        elif(userRole == 2):
            print("Advisor")
        elif(userRole == 1):
            print("Professor")
        else:
            print("Student")
        '''
    else:
        Login.signUp()

