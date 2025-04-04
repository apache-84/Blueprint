from Course import Course
from CourseData import getCourse, updateCourse, checkCourseID
from Announcement import Announcement
from AnnouncementData import postAnnouncement, getAnnouncement, updateEditHistory
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
            0 - Leave the course editor
            1 - Edit the course ID
            2 - Edit the course name
            3 - Edit the course description
            4 - Edit the course sections
            5 - Edit the recommended year for the course
            6 - Edit the offered terms for the course
            """)
            match command:
                case 0: # Leave the course editor
                    print("Leaving the course editor.")
                case 1: # Edit the course ID
                    cid = input("Enter a course ID (e.g. CSCI 260): ").upper()      
                    if checkCourseID(cid) == False:
                        print("Course with that ID already exists within database. Can't change ID to that!")
                    elif len(cid) < 1 or len(cid) > 10:
                        print("Course ID is not of the correct format.")
                    else:
                        c.setID(cid)
                case 2: # Edit the course name
                    name = input("Enter the name of the course in full (e.g. Topics in Computer Science): ")
                    if len(name) < 1 or len(name) > 50:
                        print("Course name is empty or too long, please retry.")  
                    else:
                        self.setName(name)
                case 3: # Edit the course description
                    desc = input("Enter a description of the course: ")
                    if (len(cid) > 1000):
                        print("Description is too long, description should be less than 1000 characters.")
                    else:
                        self.setDescription(desc)
                case 4: # Edit the course sections
                    sections = input("Enter the sections and schedule of a course (E.g. S25N01 - Mo We 11:30-13:00): ")
                    if (len(sections) < 1):
                        print("You must enter atleast one section.")
                    else:
                        self.setSections(sections)
                case 5: # Edit the recommended year for the course
                    try:
                        year = int(input("Enter the recommended year that this course be taken by students (1,2,3,4): "))
                        if (year >= 1 or year <= 4):
                            self.setRecYear(year)
                        else:
                            print("Invalid input, please enter a single digit number between 1-4.")
                    except ValueError:
                        print("Value is of incorrect data type, try again.")
                case 6: # Edit the offered terms for the course
                    try:
                        term = int(input("""Enter the term this course is offered in:
                                        1 - Fall
                                        2 - Spring
                                        3 - Both
                                        """))
                        match term:
                            case 1:
                                self.setTerm("Fall") 
                            case 2:
                                self.setTerm("Spring")  
                            case 3:
                                self.setTerm("Both")   
                            case _:
                                print("Please select either 1, 2, or 3.")
                    except ValueError:
                        print("Value is of incorrect data type, try again.")
                case _: # Invalid command input
                    print("Invalid input, try again!")

        # Update edit history and make announcement.
        updateEditHistory(self.getID(), cid)


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
        print("Course succesfully added to your profile!!!")
        
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
