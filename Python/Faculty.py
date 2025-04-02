from Course import Course
from CourseData import getCourse, updateCourse
from Announcement import Announcement
from AnnouncementData import postAnnouncement, getAnnouncement

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

    def register(self):

        #Get the username
        while True:
            user = input("Enter a username between 1-20 digits:")
            if (len(user) == 0 or len(user) > 20):
                print("Username is not between 1-20, please try again")
            else:
                self.__username = user
                break
                
        while True:
            pWord = hash(input("Enter a password:"))
            print(pWord) # REMOVE LATER PLEASE GOD REMOVE REMOVE THIS PLEASE PLEASE PLEASE DONT LEAVE THIS REMOVE IT AT ALL COSTS
            if (len(pWord == 0)):
                print("Password must be longer than 0 characters!")
            else:
                self.__password = pWord
                break
        
    def makeAnnouncement(self):
        """
        Faculty member makes announcement and it gets posted to database.
        """