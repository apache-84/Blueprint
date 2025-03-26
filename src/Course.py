from Review import Review
from ReviewData import getReview

class Course():
    """
    Creates a course object that can be added to the database or displayed to the frontend.

    This object gets all reviews for a given class, calculates appropriate values, and stores them.
    """
    def __init__(self, id: int = 0, name: str = "", description: str="", diff: float = 0.0, hours: float = 0.0, sections: str = "", year: int = 0, ):
       self.__courseID = id
       self.__courseName = text
       self.__ = diff
       self.__recHours = hours
       self.__reviewDate = date