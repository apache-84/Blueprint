from flask import session, flash, url_for
from .db_queries import *
from .Student import Student
from .Faculty import FacultyMember
from .StudentData import *
from .FacultyData import *
from .PinnedCoursesData import getPinnedCourses
from .CourseData import checkCourseID, getCourse
import hashlib
from markupsafe import Markup

class SelectCourseError(Exception): pass
class UsernameTakenError(Exception): pass
class UsernameNotFoundError(Exception): pass
class IncorrectPasswordError(Exception): pass
class UserTypeError(Exception): pass

# FUNCTIONS FOR LOGIN SYSTEM

def registerUser(userType: str, username: str, password: str):

    if checkUsername(userType, username) == True:
        if userType == "S":
            student = registerStudent(username, password)
            session['userType'] = userType
            session['username'] = student.getUsername()
            session['userID'] = student.getID()
        if userType == "F":
            faculty = registerFaculty(username, password)
            session['userType'] = userType
            session['username'] = faculty.getUsername()
            session['userID'] = faculty.getID()
            initPinnedCourses()
    else:
        login_url = url_for('login')
        raise UsernameTakenError(Markup(f"An account with that username already exists.<br>" 
                                        f"Please choose another username or try <a href='{login_url}'>logging in</a>."))

def loginUser(userType: str, username: str, password: str):

    if checkUsername(userType, username) == True:
        if userType == "S":
            raise UsernameNotFoundError("A student account with that username doesn't exist.")
        elif userType == "F":
            raise UsernameNotFoundError("A faculty member account with that username doesn't exist.")
    else:
        if checkPassword(userType, username, password):
            if userType == "S":
                student = stuToDict(getStudent(username))
                session['userType'] = userType
                session['username'] = student['username']
                session['userID'] = student['id']
            elif userType == "F":  
                faculty = facToDict(getFaculty(username))
                session['userType'] = userType
                session['username'] = faculty['username']
                session['userID'] = faculty['id']
                initPinnedCourses()
            else:
                session['userType'] = "G"
                session['username'] = ""
                session['userID'] = ""
        else:
            raise IncorrectPasswordError("Password is incorrect.")
            
def getCurrentUser():
    userType = session.get('userType')
    userID = session.get('userID')
    username = session.get('username')

    if userType == 'S':
        return Student(userID, username)
    elif userType == 'F':
        return FacultyMember(userID, username, "", getPinnedCourses(userID))
    return None  # not logged in

def checkUsername(userType: str, username: str) -> bool:
    """
    Checks if an account with username exists. Returns true if username isn't taken, false if it is.
    """
    if userType == "S":
        sql = "select * from Students where username = ?"
        res = fetch_query(sql, username)
        return len(res) == 0
    elif userType == "F":
        sql = "select * from FacultyMembers where username = ?"
        res = fetch_query(sql, username)
        return len(res) == 0
    return False

def checkPassword(userType: str, username: str, password: str) -> bool:
    """
    Checks if an account with a given username gave the correct password. True if correct, false if not.
    """
    # Hash the password
    p = hashlib.sha256(password.encode()).hexdigest()
    
    # Get other password from db
    if userType == "S":    
        sql = "select password from Students where username = ?"
        res = fetch_query(sql, username)
    elif userType == "F":
        sql = "select password from FacultyMembers where username = ?"
        res = fetch_query(sql, username)
    else: 
        return False
    DBPassword = res[0][0]

    return p == DBPassword


# FUNCTIONS FOR SELECTED COURSES

def initSelectedCourses():
    """
    Checks if the user has a selected courses list, if not, initializes one for them.
    """

    if 'selected_courses' not in session:
        session['selected_courses'] = []

def calculateSemesterData(courseIDs: list[str]):
    """
    Calculates the semester data from a users's selected courses list.
    
    Returns a 2-element list containing the total recommended hours per week and average difficulty of the selected courses.
    Index 0 is the total hours per week, index 1 is the semester's average difficulty.
    :return: A list of the results in the format described above, named 'semesterData'.
    """

    # Sanity check
    if len(courseIDs) == 0:
        return

    dsum = 0.0
    semesterData = [0.0, 0.0]

    for cid in courseIDs:
        course = getCourse(cid)

        dsum += course.getDifficulty()
        semesterData[0] += course.getHours()
    
    semesterData[1] = dsum / len(courseIDs)

    # Rounding to one decimal place.
    semesterData[1] = round(semesterData[1], 1)
    semesterData[0] = round(semesterData[0], 1)
    return semesterData

def selectCourse(cid: str): 
    """
    Selects a course to be stored in selected courses, given a course ID.
    
    Get a courseID, check that the courseID exists and then append the corresponding Course object with the given courseID to selectedCourses.
    """
    
    courses = session.get('selected_courses')

    if checkCourseID(cid) == True:
        if len(courses) > 0 and cid in courses:
            raise SelectCourseError("You have already selected that course! Can't add it to your semester.")
        courses.append(cid)
        session['selected_courses'] = courses
        print(cid, "added to your semester!")
    elif checkCourseID(cid) == False:
        raise SelectCourseError("Course not found in database. Reload the page and try again.")


# FUNCTIONS FOR PINNED COURSES

def initPinnedCourses():
    """
    Checks if the user has a pinned courses list, if not, initializes one for them.
    """
    if session.get('userType') != "F":
        raise UserTypeError("User is of incorrect type, must be a faculty user to pin courses.")
    
    if 'pinned_courses' not in session:
        session['pinned_courses'] = []