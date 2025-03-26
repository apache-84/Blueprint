import sqlite3

from db_queries import fetch_query, execute_query
from Review import Review
from CourseData import checkCourseID, getCourse, updateCourse
from Course import Course

def writeReview(r: Review, cid: str): # Student s and Course c
    """
    Writes a review to the database given a Review object and a valid course ID. Also updates course values.


    First checks if the course ID is for an existing course. If the course exists, then it inserts the review into the database.
    After database insertion, the course's difficulty and hours values are updated and written to the database as well.
    :param r: The review to be written to the database.
    :param cid" The course ID of the review.
    """
    if checkCourseID(cid) == False:
        print{"Course with the given ID doesn't exist in the database."}
        return

    id = findNextID()
    difficulty = r.getDifficulty()
    hours = r.getHours()
    date = r.getDate()
    text = r.getText()
    # student = s.getID()

    sql = "insert into Reviews values (?, ?, ?, ?, ?, ?)" # ?
    execute_query(sql, id, text, difficulty, hours, date, cid) # student
    print("Review for", cid, "submitted succesfully with ID", id)

    # After review has been inserted, update course difficulty and hours values:
    course = getCourse(cid)
    course.calculateAverages()
    course.updateCourse()

    
def deleteReview(id: int): # deletes a review given an id
    """
    Deletes a review from the database given a reviewID

    :param id: The reviewID of the review to be deleted.
    """
    sql = "delete * from Reviews where reviewID = ?"
    execute_query(sql, id)

def getReview(id: int) -> Review:
    """
    Retrieves a review from the database given a reviewID

    This method finds a review from the database and then constructs a Review object to be displayed on the frontend.
    :param id: The reviewID of the review to be retrieved.
    :return: The retrieved review as a Review object.
    """
    sql = "select * from Reviews where reviewID = ?"
    print(fetch_query(sql, id))
    res = fetch_query(sql, id)[0] # first row of result set
    review = Review(res[0], res[1], res[2], res[3], res[4]) # first 5 column values
    return review

def findNextID() -> int:
    """
    Finds the next reviewID to use in the database.

    The next reviewID will be 1 greater than the maximum ID value already existing within 
    the Reviews table in the database.
    :return: The reviewID to be used for the next review.
    """
    sql = "select max(reviewID) from Reviews"
    res = fetch_query(sql)[0]
    if res[0] == None:
        id = 1
    else:
        id = res[0] + 1

    return id

# Run this to create a review through the command line, write it to the database, and retrieve it from the database!
if __name__ == '__main__':
    id = findNextID()

    r = Review()
    r.createReview()
    writeReview(r)

    print(getReview(id))