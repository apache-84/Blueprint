from flask import session, flash, url_for
from .db_queries import *
from .Student import Student
from .Faculty import FacultyMember
from .StudentData import *
from .FacultyData import *
from .CoursesTaughtData import getCoursesTaught
from .CourseData import checkCourseID, getCourse
import hashlib
from markupsafe import Markup

class SelectCourseError(Exception): pass
class UsernameTakenError(Exception): pass
class UsernameNotFoundError(Exception): pass
class IncorrectPasswordError(Exception): pass


def registerUser(userType: str, username: str, password: str):

    if checkUsername(userType, username) == True:
        if userType == "S":
            student = registerStudent(username, password)
            session['user_type'] = userType
            session['username'] = student['username']
            session['user_id'] = student['id']
        if userType == "F":
            faculty = registerFaculty(username, password)
            session['user_type'] = userType
            session['username'] = faculty['username']
            session['user_id'] = faculty['id']
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
                session['user_type'] = userType
                session['username'] = student['username']
                session['user_id'] = student['id']
            elif userType == "F":  
                faculty = facToDict(getFaculty(username))
                session['user_type'] = userType
                session['username'] = faculty['username']
                session['user_id'] = faculty['id']
            else:
                session['user_type'] = "G"
                session['username'] = ""
                session['user_id'] = ""
        else:
            raise IncorrectPasswordError("Password is incorrect.")

            
def getCurrentUser():
    user_type = session.get('user_type')
    user_id = session.get('user_id')
    username = session.get('username')

    if user_type == 'S':
        return Student(user_id, username)
    elif user_type == 'F':
        return FacultyMember(user_id, username, "", getCoursesTaught(user_id))
    return None  # not logged in


"""
Checks if an account with username exists. Returns true if username isn't taken, false if it is.
"""

def checkUsername(userType: str, username: str) -> bool:
    if userType == "S":
        sql = "select * from Students where username = ?"
        res = fetch_query(sql, username)
        return len(res) == 0
    elif userType == "F":
        sql = "select * from FacultyMembers where username = ?"
        res = fetch_query(sql, username)
        return len(res) == 0
    return False

"""
Checks if an account with a given username gave the correct password. True if correct, false if not.
"""

def checkPassword(userType: str, username: str, password: str) -> bool:
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

def calculateSemesterData():
    """
    Calculates the semester data from a users's selected courses list.
    
    Returns a 3-element list containing the selected courses, average difficulty, and total recommended hours per week.
    Index 0 is a list of Course objects, index 1 is the semester's average difficulty, index 2 is the total hours per week.
    :return: A list of the results in the format described above, named 'semesterData'.
    """
    courses = session.get('selected_Courses')

    dsum = 0.0
    semesterData = [[], 0.0, 0.0]

    for cid in courses:
        course = getCourse(cid)

        dsum += course.getDifficulty()
        semesterData[2] += course.getHours()
        semesterData[0].append(course)
    
    semesterData[1] = dsum / len(courses)

    # Rounding to one decimal place.
    semesterData[1] = round(semesterData[1], 1)
    semesterData[2] = round(semesterData[2], 1)
    return semesterData

def selectCourse(cid: str): 
    """
    Selects a course to be stored in selected courses, given a course ID.
    
    Get a courseID, check that the courseID exists and then append the corresponding Course object with the given courseID to selectedCourses.
    """
    
    courses = session.get('selected_Courses')

    if checkCourseID(cid) == True:
        if cid in courses:
            raise SelectCourseError("You have already selected that course! Can't add it to your semester.")
        courses.append(cid)
        session['selected_courses'] = courses
        print(cid, "added to your semester!")
    elif checkCourseID(cid) == False:
        raise SelectCourseError("Course not found in database. Reload the page and try again.")


