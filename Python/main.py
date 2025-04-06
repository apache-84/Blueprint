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
from datetime import datetime

if __name__ == '__main__':
    try:
        print ("Hello, Welcome to Blueprint.viu.cs")
    
        # While loop for login and registry
        facultyFlag = False
        studentFlag = False
        while True:
            res = input("Are you a student or faculty member? Type S for Student or F for faculty. ").upper()
            if res == 'F':
                f = loginFaculty()
                if type(f) == FacultyMember:
                    facultyFlag = True
                break
            elif res == 'S':
                s = loginStudent()
                if type(s) == Student:  
                    studentFlag = True
                break
            else:   
                print("Incorrect input, please enter S or F")

        # Successfully logged in as a Faculty member, now presenting all options available to interact
        
        if (facultyFlag == True):
            command = -1
            while command != '0':
                command = input("""Type the following number to do the following action:
                0 - End your session 
                1 - View a course
                2 - Add a course to your courses taught.
                3 - Add a course
                4 - Edit a course
                5 - Create an announcement for a course
                """)
                match command:
                    case '0':
                        print("Thank you for visiting! Enjoy your day!!! :)")
                    case '1':
                        courseRes = input("Search what course you would like to find: ").upper()
                        if (checkCourseID(courseRes) == True):
                            course = getCourse(courseRes)
                                        
                            print("Course ID: ", course.getID())
                            print("Course Name: ", course.getName())
                            print("Course Description: ", course.getDescription())
                            print("Recommended Hours: ", course.getHours())
                            print("Course Difficulty: ", course.getDifficulty())
                            print("Course Sections: ", course.getSections())
                            print("Recommended year: ", course.getRecYear())
                            print("Course Term: ", course.getTerm())
                            
                        else:
                            print("invalid search, please try another courseID: ")
                            
                    case '2': 
                        addCourseTaught = input("Enter a course that you've taught: ")                
                        f.addCourseProfile(addCourseTaught)

                    case '3':
                        f.addCourse()
                    
                    case '4':
                        editID = input("Enter the courseID of the course you would like to edit: ")
                        if (checkCourseID(editID) == True):
                            f.editCourse(editID)
                        else:
                            print("Invalid course ID, please try again. ")
                        
                    case '5':
                        f.makeAnnouncement()
                        
                    case _:
                        print("Invalid command! Try again.")


        # Student menu prior to login check            
        if (studentFlag == True):
            command = -1
            while command != '0':
                command = input("""Type the following number to do the following action:
                0 - End your session
                1 - View a course
                2 - Add a course
                3 - Calculate your Semester
                4 - Add a review 
                5 - Edit a review you've made
                6 - View the announcements board
                7 - View all of your posted reviews
                """)
                match command:
                    case '0':
                        print("Thank you for visiting! Enjoy your day!!! :)")
                    case '1':
                        courseRes = input("Search what course you would like to find: ")
                        if (checkCourseID(courseRes) == True):
                            course = getCourse(courseRes)
                            cmd = -1
                            print("Welcome to the course viewer for {c}!".format(c = course.getID()))
                            while cmd != '0':
                                cmd = input("""Type the following number to do the following action:
                                0 - Leave the course viewer.
                                1 - View course information (without description)
                                2 - View course description
                                3 - View course reviews
                                4 - View course announcements
                                """)
                                
                                match cmd:
                                    case '0':
                                        print("Thank you for using the course viewer! Going back to the main page.")
                                    case '1':
                                        print("Course ID:", course.getID())
                                        print("Course Name:", course.getName())
                                        print("Recommended Hours Per Week:", course.getHours())
                                        print("Course Difficulty:", course.getDifficulty())
                                        print("Course Sections:", course.getSections())
                                        print("Recommended year:", course.getRecYear())
                                        print("Course Term:", course.getTerm())
                                    case '2':
                                        print(course.getID(), "Course Description: \n" + course.getDescription())
                                    case '3':
                                        reviewList = getReviewData(course.getID())

                                        for review in reviewList:
                                            print("ID:", review.getID())
                                            print("Difficulty:", review.getDifficulty())
                                            print("Recommended hours per week", review.getHours())
                                            print("Review: \n" + review.getText())
                                            print("\n")
            
                                    case '4':
                                        pass
                                    case _:
                                        print("Invalid command! Try again")


                            print("Course ID: ", course.getID())
                            print("Course Name: ", course.getName())
                            print("Course Description: ", course.getDescription())
                            print("Recommended Hours Per Week: ", course.getHours())
                            print("Course Difficulty: ", course.getDifficulty())
                            print("Course Sections: ", course.getSections())
                            print("Recommended year: ", course.getRecYear())
                            print("Course Term: ", course.getTerm())
                            
                        else:
                            print("invalid search, courseID not found... Returning to main page. ")
                            
                    case '2':
                        s.selectCourse()
                                            
                    case '3':
                        courseList = s.calculateSemesterData()   

                        courses = s.getSelCourses()
                        for course in courses:
                    
                            print("Course ID: ", course.getID())
                            print("Course Name: ", course.getName())
                            print("Course Description: ", course.getDescription())
                            print("Recommended Hours: ", course.getHours())
                            print("Course Difficulty: ", course.getDifficulty())
                            print("Course Sections: ", course.getSections())
                            print("Recommended year: ", course.getRecYear())
                            print("Course Term: ", course.getTerm())
                        print(courseList) 
                        
                    case '4':
                        s.makeReview()

                    case '5':
                        s.editReview()
                    
                    case _:    
                        print("Invalid command! Try again")
        #successfully logged in now select an action    

                
        print("Thanks for using Blueprint.viu.cs!")
    except Exception as e:
        print("Program ran into an error, terminating...")
        print(e)