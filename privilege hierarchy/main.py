import connection
import Login
import DBfuncs

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



if __name__ == "__main__":

    #viewFaculty()
    #viewCourses()
    #viewStudents()

    getRole("Antonio")

    #Signup.userExists("Antonio")
    addFaculty("Ant", "D", "adipio_stu@kent.edu", "code")  # works

    addUser("Antonio", "1234", 4)
    userType = input("Are you a new user or a returning user? [N/R]")

    if(userType == "R"):
        Signup.login()
    else:
        Signup.signUp()

    addUser("Antonio", "1234", 4)
    addFaculty("Ant", "D", "adipio_stu@kent.edu", "code") #works
    addCourse("className", "professorName", "studentList", 1, 13, 16, 32, "numStudents", "syllabus") #works
    addStudent("firstName", "lastName", 1, 16, 2021, 23, "Eddy") #works