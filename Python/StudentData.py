from Student import Student
from db_queries import *
from ReviewData import getReview
from Review import Review
import hashlib

def registerStudent():
    """
    Asks the student for their username and password, hashes the password, gets the next available student ID, and stores it to the database.
    """
    s = Student()
    s.register()

    s.setID(getNextID())

    sql = "insert into Students values (?, ?, ?)"

    execute_query(sql, s.getID(), s.getUsername(), s.getPassword())
    print("Student registered to database!")

def getReviews(stuID: int) -> list[Review]:
    """
    Returns a list of all the Review objects a student has written.

    :param stuID: The ID of the student whose reviews are being retrieved.
    """
    sql = "select reviewID from Reviews where studentID = ?"
    reviews = fetch_query(sql, stuID)
    stuReviews = []
    for review in reviews:
        stuReviews.append(getReview(review))

    return stuReviews

def getNextID() -> int:
    """
    Finds the next studentID to use in the database.

    The next studentID will be 1 greater than the maximum ID value already existing within 
    the Students table in the database.
    :return: The studentID to be used for the next student.
    """
    sql = "select max(studentID) from Students"
    res = fetch_query(sql)[0]
    if res[0] == None:
        id = 1
    else:
        id = res[0] + 1

    return id

def checkIfReacted(stuID: int, annID: int) -> int:
    """
    Checks if a student has already reacted to an announcement.

    :return: -1 if the student hasn't reacted to the announcement. 0 if they downvoted, 1 if they upvoted the announcement.
    """
    sql = "select reaction from AnnouncementReactions where studentID = ? and announcementID = ?"
    res = fetch_query(sql, stuID, annID)
    if (len(res) == 0):
        return -1
    
    return res[0]

def updateReaction(stuID: int, annID: int, reaction: int):
    status = checkIfReacted(stuID, annID)
    
    unreactSQL = "delete from AnnouncementReactions where studentID = ? and AnnouncementID = ?"
    reactSQL = "update reaction from AnnouncementReactions where studentID = ? and AnnouncementID = ?"
    
    insertSQL = "insert into AnnouncementReactions"
    
    if status == 0:
        if reaction == 0:
            execute_query(unreactSQL)
        elif reaction == 1:
            execute_query(reactSQL, reaction)
    elif status == 1:
        if reaction == 0:
            execute_query(reactSQL, reaction)
        elif reaction == 1:
            execute_query(unreactSQL)
    else:
        execute_query(insertSQL)
        

def loginStudent() -> Student:
    user = input("Enter your username: ")
    sql = "select * from Students where username = ?"
    res = fetch_query(sql, user)
    
    if (len(res) == 0):
        print("An account with this username doesn't exist, want to register an account?")
        while True:
            ans = input("Y/N: ").upper()
            if ans == "Y":
                registerStudent()
                loginStudent()
                break
            elif ans == "N":
                break
    res = res[0]
    
    id = res[0]
    username = res[1]
    password = res[2]
    
    pWord = input("Enter your password: ")
    p = hashlib.sha256()
    p.update(pWord)
    pWord = hash
    print(pWord)
    
    if pWord != password:
        print("Incorrect password, please try again.")
        return
    
    s = Student(id, username, password)
    
    return s

if __name__ == '__main__':
    loginStudent()