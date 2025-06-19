from .Course import Course
from .CourseData import *
from .db_queries import *

def getPinnedCourses(facID: int) -> list[Course]:
    """
    Gets all of the courses taught for a specific faculty member account.

    :param facID: The faculty member's ID.
    :return: A list of Course objects that the faculty member has added to their 'courses taught'.
    """
    pinnedCourses = []
    sql = "select courseID from CoursesTaught where facultyID = ?"
    res = fetch_query(sql, facID)
    for course in res:
        if checkCourseID(course[0]) == True:
            c = getCourse(course[0])
            pinnedCourses.append(c)
    
    return pinnedCourses

def addPinnedCourses(facID: int, cid: str):
    """
    Adds a faculty member's selected course that they teach to the database.
    
    :param facID: The faculty member's ID.
    :param cid: The course ID of the course they want to add.
    """

    sql = "insert into CoursesTaught values (?, ?)"
    execute_query(sql, cid, facID)

def delPinnedCourses(facID: int, cid: str):
    """
    Removes a faculty member's selected course that they teach from the database.

    :param facID: The faculty member's ID.
    :param cid: The course ID of the course they want to remove.
    """
    sql = "delete from PinnedCourses where courseID = ? and facultyID = ?"
    execute_query(sql, cid, facID)
