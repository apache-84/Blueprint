from Announcement import *
from AnnouncementData import *
from Review import *
from ReviewData import *
from Course import *
from CourseData import *
from Student import *
from StudentData import *
from Faculty import *
from FacultyData import *
from CoursesTaughtData import *

if __name__ == '__main__':
    print ("Hello, Welcome to Blueprint.viu.cs")
   
    # While loop for login and registry
    facultyFlag = False
    studentFlag = False
    while True:
        res = input("Are you a student or faculty member? Type S for Student or F for facult").upper()
        if res == 'F':
            f = loginFaculty()
            facultyFlag = True
            break
        elif res == 'S':
            s = loginStudent()
            studentFlag = True
            break
        else:   
            print("Incorrect input, please enter S or F")

    if (facultyFlag = True):
        while command != 0:
            command = input("""Course editor: Type the following number to do the following action:
            0 - End your session
            1 - View a course
            2 - Add a course to your courses taught.
            3 - Add a course
            4 - Edit a course
            5 - Create an announcement for a course
            """)
            match command:
                case 0:
                    print("Thank you for visiting! Enjoy your day!!! :)")
                case 1:
                    courseRes = input("Search what course you would like to find: ")
                    if (checkCourseID(courseRes) == True):
                        getCourse(courseRes)
                        break
                    else:
                        print("invalid search, please try another courseID: ")
                        
                case 2: 
                    addCourse = input("Enter a course that you've taught: ")                
                    f.addCourseProfile(addCourse)

                case _:
                    print("Invalid command! Try again")

    #successfully logged in now select an action    
    print("Select what action you would like to do?: ")
        case 0:
            
        case 1:
            
        case 2:
        case 3:
        case 4:
            
        
    
