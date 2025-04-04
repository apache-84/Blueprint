from Course import Course
from CourseData import getCourse, updateCourse, checkCourseID
from Announcement import Announcement
from AnnouncementData import postAnnouncement, getAnnouncement
from CoursesTaughtData import addCoursesTaught, delCoursesTaught
import hashlib

class FacultyMember():

    def __init__(self, id: int = 0, username: str = "", password: str = "", courses: list[Course] = []):
        """
        Instantiates a FaculyMember user object with the given values: facID, username, password (hashed), and a list of courses taught. Otherwise, will use default values.

        :param id:  The faculty member's unique ID.
        :param username: The faculty members's account username.
        :param password: The faculty members's encrypted password.
        :param courses: A list of courses that the faculty member teaches.
        """
        self.__facID = id
        self.__username = username
        self.__password = password
        self.__coursesTaught = courses
    
    # Getter methods:
    def getID(self) -> int:
        return self.__facID
    
    def getUsername(self) -> str:
        return self.__username
        
    def getPassword(self) -> str:
        return self.__password
            
    def getID(self):
        return self.__facID

    def getCourses(self) -> list[Course]:
        return self.__coursesTaught

    # Setter methods:
    def setID(self, id: str):
        self.__facID = id

    def setUsername(self, username: str):
        self.__username = username
    
    def setPassword(self, password: int):
        self.__password = password
        
    def setCourses(self, courses: list[Course]):
        self.__coursesTaughts = courses

    def editCourse(self, cid: str):
        """
        From a given course ID, allows faculty to alter one (per call) of the following 
        fields of a course: id, name, description, sections, recYear, term. 

        idk how we want to do this
        
        :param cid: The ID of the course whose information is being edited.
        """
        command = -1
        c = getCourse(cid)
        while command != 0:
            command = input("""Course editor: Type the following number to do the following action:
            1 - Edit the course ID
            2 - Edit the course name
            3 - Edit the course description
            4 - Edit the course sections
            5 - Edit the recommended year for the course
            6 - Edit the offered terms for the course
            0 - Leave the course editor
            """)
            match command:
                case 0: # Leave the course editor
                    print("Leaving the course editor.")
                    break
                case 1: # Edit the course ID
                    while True:
                        cid = input("Enter a course ID (e.g. CSCI 260): ").upper()
                        
                        if checkCourseID(cid) == False:
                            print("Course with that ID already exists within database. Can't change ID to that!")
                        elif len(cid) < 1 or len(cid) > 10:
                            print("Course ID is not of the correct format.")
                        else:
                            c.setID(cid)
                            break
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case _:
                    print("Invalid input, try again!")


    def register(self):
        """
        Allows a faculty member to input their username and password for account registration.
        """
        # Get the username
        while True:
            user = input("Enter a username between 1-20 digits: ")
            if len(user) == 0 or len(user) > 20:
                print("Username is not between 1-20, please try again")
            else:
                self.__username = user
                break

        # Get the password 
        while True:
            pWord = input("Enter a password: ")
            if len(pWord) == 0:
                print("Password must be longer than 0 characters!")
            else:
                self.__password = hashlib.sha256(pWord.encode()).hexdigest()
                break
        
    def makeAnnouncement(self):
        """
        Allows a faculty member to make an announcement. Announcement gets posted to database.
        """
        a = Announcement()    
        a.createAnnouncement()
        postAnnouncement(a, self.getID())

    def addCourseProfile(self):
        """
        Allows a faculty member to add a course to their profile under 'courses taught'. Gets added to CoursesTaught table in database.
        """
        cid = input("Enter the course ID of the course you want to add to your taught courses: ")
        if checkCourseID(cid) == False:
            print("Course", cid, "does not exist")
            return
        
        addCoursesTaught(self.getID(), cid)
        print ("Course succesfully added to your profile!!!")
        
    def removeCourseProfile(self):
        """
        Allows a faculty member to remove a course from their profile if it is already in their profile. Gets removed from CoursesTaught table in database.
        """
        
        cid = input("Enter the course ID of the course you want to remove: ")
        
        # Checks if course ID is in their coursesTaught already.
        courseCheck = False
        for course in self.getCourses():
            if cid == course.getID():
                courseCheck = True
                break

        if courseCheck == False:
            print("Course", cid, "is not in your courses tauught!")
            return
        
        delCoursesTaught(self.getID(), cid)
