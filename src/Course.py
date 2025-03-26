from Review import Review
from ReviewData import getReview

class Course():
    """
    Creates a course object that can be added to the database or displayed to the frontend.

    This object gets all reviews for a given class, calculates appropriate values, and stores them.
    """
    
    def __init__(self, id: int = 0, name: str = "", desc: str="", diff: float = 0.0, hours: float = 0.0, sections: str = "N/A", year: int = 0, term: str = "N/A" ):
        """
        Instantiates a Course object with the given values: id, name, desc, diff, hours, sections, year, term. Otherwise, will use default values.

        :param id: The course's ID.
        :param name: The course's name - E.g. 'CSCI 260'.
        :param diff: The course's difficulty rating.
        :param hours: The hours per week recommendation to be successful in this course.
        :param sections: The course's sections for the term and their schedules.
        :param year: The recommended year this course should be taken in.
        :param term: The term that the course is offered in ('Spring', 'Fall' or 'Both'). Note that CSCI classes aren't offered in the summer term.
        """
       self.__courseID = id
       self.__courseName = name
       self.__description = desc
       self.__difficulty = diff
       self.__recHours = hours
       self.__sections = sections
       self.__recYear = year
       self.__term = term

    