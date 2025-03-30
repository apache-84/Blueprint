from datetime import datetime
from CourseData import checkCourseID


class Announcement():
    def __init__(self, annID: int = 0, annText: str = "", annDate: str = "", cid: str = ""):
       self.__annID = annID
       self.__annText = annText
       self.__annDate = annDate
       self.__courseID = cid

    #Getter methods
    def getAnnID(self) -> int:
        return self.__annID

    def getAnnText(self) -> str:
        return self.__annText

    def getAnnDate(self) -> str:
        return self.__annDate

    def getCourse(self) -> str:
        return self.__courseID

    #Setter Methods
    def setAnnID(self, aid: str):
        self.__annID = aid

    def setAnnText(self, atext: str):
        self.__annText = atext

    def setAnnDate(self, adate: str):
        self.__annDate = adate
        
    def setCourse(self, course: str):
        self.__courseID = course

    def createAnnouncement(self):
        """
        Creates a course object
        prompts user to enter a courseID, calls checkCourseID to ensure course exists in database,
        then prompts user to enter the announcement text,
        and then sets the announcement date to the current day
        """
        # Get course section
        while True:
            cid = input("What course is this review for (e.g. CSCI 260)? ").upper()

            if checkCourseID(cid):
                self.setCourse(cid)
                break
            else:
                print("Course doesn't exist within the database! Try again..")
        while True:
            text = input("Enter the text to your announcement post, between 1-500 characters: ")
            if (len(text) < 1 or len(text) > 500):
                print("Announcement text size is not correct, please enter between 1-500 characters")
            else:
                self.setAnnText(text)
                break
        
        self.setAnnDate(str(datetime.today().date()))

    

    