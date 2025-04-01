from Faculty import FacultyMember
from db_queries import *

def register():
    """
    Asks the faculty member for their username and password, hashes the password, gets the next available faculty ID, and stores it to the database.
    """
    f = FacultyMember()
    f.register()

    f.setID(getNextID())

    sql = "insert into Students values (?, ?, ?)"

def getCoursesTaught(facID: int):
    pass

def getNextID() -> int:
    """
    Finds the next facultyID to use in the database.

    The next facultyID will be 1 greater than the maximum ID value already existing within 
    the FacultyMembers table in the database.
    :return: The facultyID to be used for the next student.
    """
    sql = "select max(facultyID) from FacultyMembers"
    res = fetch_query(sql)[0]
    if res[0] == None:
        id = 1
    else:
        id = res[0] + 1

    return id