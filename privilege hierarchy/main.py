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
                print("[viewCourses], [viewStudents], [changeRole], [enrollStudent], [coursesIn], [studentsIn]")
                input = input("Selection:")
                if(input == "addUser"):
                    DBfuncs.addUser()
                elif(input == "addFaculty"):
                    DBfuncs.addFaculty()
                elif(input == "addCourse"):
                    DBfuncs.addCourse()
                elif(input == "addStudent"):
                    DBfuncs.addStudent()
                elif(input == "deleteCourse"):
                    DBfuncs.deleteCourse()
                elif(input == "deleteStudent"):
                    DBfuncs.deleteStudent()
                elif(input == "viewFaculty"):
                    DBfuncs.viewFaculty()
                elif(input == "viewCourses"):
                    DBfuncs.viewCourses()
                elif(input == "viewStudents"):
                    DBfuncs.viewStudents()
                elif(input == "changeRole"):
                    DBfuncs.changeRole()
                elif(input == "enrollStudent"):
                    studentid = input ("Enter student id:")
                    courseid = input ("Enter course id:")
                    DBfuncs.enrollStudent(studentid,courseid)
                elif(input == "coursesIn"):
                    studentid = input("Enter student id:")
                    DBfuncs.viewCoursesIn(studentid)
                elif(input == "studentsIn"):
                    courseid = input("Enter course id:")
                    DBfuncs.viewStudentsIn(courseid)
            case 3:
                print("Dean")
                print("What would you like to do [addFaculty], [addCourse], [addStudent], [deleteCourse], [deleteStudent], [viewFaculty]")
                print("[viewCourses], [viewStudents], [enrollStudent], [coursesIn], [studentsIn]")
                input = input("Selection:")
                if(input == "addFaculty"):
                    DBfuncs.addFaculty()
                elif(input == "addCourse"):
                    DBfuncs.addCourse()
                elif(input == "addStudent"):
                    DBfuncs.addStudent()
                elif(input == "deleteCourse"):
                    DBfuncs.deleteCourse()
                elif(input == "deleteStudent"):
                    DBfuncs.deleteStudent()
                elif(input == "viewFaculty"):
                    DBfuncs.viewFaculty()
                elif(input == "viewCourses"):
                    DBfuncs.viewCourses()
                elif(input == "viewStudents"):
                    DBfuncs.viewStudents()
                elif(input == "enrollStudent"):
                    studentid = input ("Enter student id:")
                    courseid = input ("Enter course id:")
                    DBfuncs.enrollStudent(studentid,courseid)
                elif(input == "coursesIn"):
                    studentid = input("Enter student id:")
                    DBfuncs.viewCoursesIn(studentid)
                elif(input == "studentsIn"):
                    courseid = input("Enter course id:")
                    DBfuncs.viewStudentsIn(courseid)
            case 2:
                print("Advisor")
                print("What would you like to do [viewFaculty], [viewCourses], [viewStudents], [enrollStudent], [coursesIn], [studentsIn]")
                input = input("Selection:")
                if(input == "viewFaculty"):
                    DBfuncs.viewFaculty()
                elif(input == "viewCourses"):
                    DBfuncs.viewCourses()
                elif(input == "viewStudents"):
                    DBfuncs.viewStudents()
                elif(input == "enrollStudent"):
                    studentid = input ("Enter student id:")
                    courseid = input ("Enter course id:")
                    DBfuncs.enrollStudent(studentid,courseid)
                elif(input == "coursesIn"):
                    studentid = input("Enter student id:")
                    DBfuncs.viewCoursesIn(studentid)
                elif(input == "studentsIn"):
                    courseid = input("Enter course id:")
                    DBfuncs.viewStudentsIn(courseid)
            case 1:
                print("Professor")
                print("What would you like to do [viewFaculty], [viewCourses], [viewStudents], [studentsIn]")
                input = input("Selection:")
                if(input == "viewFaculty"):
                    DBfuncs.viewFaculty()
                elif(input == "viewCourses"):
                    DBfuncs.viewCourses()
                elif(input == "viewStudents"):
                    DBfuncs.viewStudents()
                elif(input == "studentsIn"):
                    courseid = input("Enter course id:")
                    DBfuncs.viewStudentsIn(courseid)
            case 0:
                print("Student")
                print("What would you like to do [viewCourses], [viewStudents]")
                input = input("Selection:")
                if(input == "viewFaculty"):
                    DBfuncs.viewFaculty()
                elif(input == "viewCourses"):
                    DBfuncs.viewCourses()
                elif(input == "viewStudents"):
                    DBfuncs.viewStudents()
                elif(input == "studentsIn"):
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

    #DBfuncs.addUser("Antonio", "1234")
    #DBfuncs.addFaculty("Ant", "D", "adipio_stu@kent.edu", "code") #works
    #DBfuncs.addCourse("test", "professorName", "studentList", 1, 13, 16, 32, "numStudents", "syllabus") #works
    #DBfuncs.addStudent("firstName", "lastName", 1, 16, 2021, 23, "Eddy") #works