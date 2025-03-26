import sqlite3

from db_queries import fetch_query, execute_query
from Review import Review

def writeReview(r: Review): # Student s and Course c
    id = findNextID()
    difficulty = r.getDifficulty()
    hours = r.getHours()
    date = r.getDate()
    text = r.getText()
    # student = s.getID()
    # course = c.getID()
    
    sql = "insert into Reviews values (?, ?, ?, ?, ?)" # ?, ?
    execute_query(sql, id, text, difficulty, hours, date) # student, course
    
    
def deleteReview(id: int): # deletes a review given an id
    sql = "delete * from Reviews where reviewID = ?"
    execute_query(sql, id)

def getReview(id: int) -> Review:
    sql = "select * from Reviews where reviewID = ?"
    res = fetch_query(sql, id)[0] # first row of result set
    review = Review()
    print(res[0], res[1], res[2], res[3], res[4])
    review.__init__(res[0], res[1], res[2], res[3], res[4]) # first 5 column values
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

if __name__ == '__main__':
    print(findNextID())
    print(sys.path)