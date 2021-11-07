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
                print("4")
            case 3:
                print("3")
            case 2:
                print("2")
            case 1:
                print("1")
            case 0:
                print("0")

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

    else:
        Login.signUp()

    DBfuncs.addUser("Antonio", "1234")
    DBfuncs.addFaculty("Ant", "D", "adipio_stu@kent.edu", "code") #works
    DBfuncs.addCourse("className", "professorName", "studentList", 1, 13, 16, 32, "numStudents", "syllabus") #works
    DBfuncs.addStudent("firstName", "lastName", 1, 16, 2021, 23, "Eddy") #works