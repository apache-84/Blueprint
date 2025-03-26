from Review import Review
from ReviewData import getReview
from CourseData import *

class Course():
    """
    Creates a course object that can be added to the database or displayed to the frontend.

    This object gets all reviews for a given class, calculates appropriate values, and stores them.
    """
    
    def __init__(self, id: int = 0, name: str = "", desc: str="", hours: float = 0.0, diff: float = 0.0, sections: str = "N/A", year: int = 0, term: str = "N/A" ):
        """
        Instantiates a Course object with the given values: id, name, desc, diff, hours, sections, year, term. Otherwise, will use default values.

        :param id: The course's ID.
        :param name: The course's name - E.g. 'CSCI 260'.
        :param desc: The course's description.
        :param diff: The course's difficulty rating.
        :param hours: The hours per week recommendation to be successful in this course.
        :param sections: The course's sections for the term and their schedules.
        :param year: The recommended year this course should be taken in.
        :param term: The term that the course is offered in ('Spring', 'Fall' or 'Both'). Note that CSCI classes aren't offered in the summer term.
        """
        self.__id = id
        self.__name = name
        self.__description = desc
        self.__recHours = hours
        self.__difficulty = diff
        self.__sections = sections
        self.__recYear = year
        self.__term = term

    # Getter methods:
    def getID(self) -> str:
        return self.__id
    
    def getName(self) -> str:
        return self.__name
  
    def getDescription(self) -> str:
        return self.__description
        
    def getDifficulty(self) -> float:
        return self.__difficulty
    
    def getHours(self) -> float:
        return self.__recHours
    
    def getSections(self) -> str:
        return self.__sections
    
    def getRecYear(self) -> int:
        return self.__recYear
    
    def getTerm(self) -> str:
        return self.__term
    
    # Setter methods:
    def setID(self, cid: str):
        self.__id = cid
    
    def setName(self, name: str):
        self.__name = name
  
    def setDescription(self, desc: str):
        self.__description = desc
        
    def setDifficulty(self, diff: float):
        self.__difficulty = diff
    
    def setHours(self, hours: float):
        self.__recHours = hours
    
    def setSections(self, sections: str):
        self.__sections = sections
    
    def setRecYear(self, year: int):
        self.__recYear = year
    
    def setTerm(self, term: str):
        self.__term = term
            
    def calcAvgDifficulty(self, rs: list):
        