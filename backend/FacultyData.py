from .Faculty import FacultyMember
from .db_queries import *
import hashlib


def updateFaculty(facID: int, username: str, password: str):
    """
    Inputs faculty member with given ID's account info into database.
    """
    sql = "update FacultyMembers set username = ?, password = ? where facultyID = ?"
    execute_query(sql, username, password, facID)


def registerFaculty(username: str, password: str) -> FacultyMember:
    """
    Takes a faculty member's username and password. Hashes the password, gets the next available student ID, and stores it to the database.
    """
    password = hashlib.sha256(password.encode()).hexdigest()
    id = getNextID()

    sql = "insert into FacultyMembers values (?, ?, ?)"
    execute_query(sql, id, username, password)

    # Create faculty member object
    f = FacultyMember(username=username, id=id)
    return f


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

def facToDict(f: FacultyMember) -> dict:
    faculty = {
    "id": f.getID(),
    "username": f.getUsername(),
    "password": f.getPassword(),
    "pinnedCourses": f.getCourses()
    }
    return faculty
    
def getFaculty(username: str):
    sql = "select * from FacultyMembers where username = ?"
    res = fetch_query(sql, username)
    if len(res) == 0:
        return None
    
    id = res[0][0]
    username = res[0][1]

    f = FacultyMember(id = id, username = username)
    return f
