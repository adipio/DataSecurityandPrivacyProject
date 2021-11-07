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
                print("[viewFaculty],[viewCourses], [viewStudents], [changeRole] idk what the last 3 functions do")
                input = input("Selection:")
                if(input == "addUser"):
                    DBfuncs.addUser()
                elif(input == "addFaculty"):
                    DBfuncs.addFaculty()
                elif(input == "addCourse"):
                    DBfuncs.addCourse()
                elif(input == "addStudent"):
                    DBfuncs.addStudent()
                elif(input == "deleteUser"):
                    DBfuncs.deleteUser()
                elif(input == "deleteFaculty"):
                    DBfuncs.deleteFaculty()
                elif(input == "deleteCourse"):
                    DBfuncs.deleteCourse()
                elif(input == "deleteStudent"):
                    DBfuncs.deleteStudent()
                elif (input == "viewFaculty"):
                    DBfuncs.viewFaculty()
                elif (input == "viewCourses"):
                    DBfuncs.viewCourses()
                elif (input == "viewStudents"):
                    DBfuncs.viewStudents()
                elif(input == "changeRole"):
                    DBfuncs.changeRole()
                else:
                    print("invalid input")

            case 3:
                print("Dean")
            case 2:
                print("Advisor")
            case 1:
                print("Professor")
            case 0:
                print("Student")

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