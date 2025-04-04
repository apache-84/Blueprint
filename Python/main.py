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
    while True:
        res = input("Are you a student or faculty member? Type S for Student or F for facult").upper()
        if res == 'F':
            loginFaculty()
            break
        elif res == 'S':
            loginStudent()
            break
        else:   
            print("Incorrect input, please enter S or F")

    #successfully logged in now select an actio    
    print("Select what action you would like to do?: ")
        case 0:
        case 1:
        case 2 
            
        
    
