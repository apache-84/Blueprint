from Course import Course
from CourseData import getCourse, updateCourse

class FacultyMember():

    def __init__(self, id: int = 0, username: str = "", password: str = "", courses: list[Course]):
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
        
    def setCourses(self, courses: list[Course]):
        self.__coursesTaughts = courses

    def editCourse(self, cid: str):
        """
        From a given course ID, allows faculty to alter one (per call) of the following 
        fields of a course: id, name, description, sections, recYear, term. 

        idk how we want to do this
        
        :param cid: The ID of the course whose information is being edited.
        """

        
