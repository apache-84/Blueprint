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


if __name__ == '__main__':
    print ("Hello, Welcome to Blueprint.viu.cs")
    while True:
        res = input("Are you a student or faculty member? Type S for Student or F for faculty").upper()
        if (res != "S" or "F"):
            print("Incorrect input, please enter S or F")
        else:
            if res == 'S':
                loginStudent()
            if res == 'F':
                loginFaculty()
