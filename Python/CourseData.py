from db_queries import fetch_query, execute_query
from Course import Course
from Review import Review
from ReviewData import getReview

def updateCourse(cid: str):
    pass

def addCourse(course: Course):
    
    pass
    
def getReviewData(cid: str) -> list[Review]:
    """
    Gets all the reviews for a course given the course ID (cid).

    First it queries for all review IDs under a given course, retrieving a list of those review IDs.
    Then for each review ID, it calls getReview() to query the review from the Reviews table and turns it into a Review class object.
    Afterwards, appends it to a list of Review class objects to be returned to the course.

    :param cid: The course ID for the course to get review data for.
    :return: A list of Review objects, where each item in the list is a review for the course.
    """
    sql = "select reviewID from Reviews where courseID = ?"
    courseReviews = fetch_query(sql, cid)
    reviewList = []
    for review in courseReviews:
        reviewList.append(getReview(review[0]))
        
    return reviewList
        
    
def getCourse(cid: str):
    pass