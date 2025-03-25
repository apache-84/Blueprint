import sqlite3
from db_queries import fetch_query, execute_query
from domainlayer import Review

def writeReview(r: Review): # Student s and Course c
    id = r.getID()
    difficulty = r.getDifficulty()
    hours = r.getHours()
    date = r.getDate()
    text = r.getText()
    # student = s.getID()
    # course = c.getID()
    
    sql = "insert into Reviews values (?, ?, ?, ?, ?)" # ?, ?
    params = (id, text, difficulty, hours, date) # student, course
    execute_query(sql, params)
    
    
def deleteReview(id: int): # deletes a review given an id
    sql = "delete * from Reviews where reviewID = ?"
    execute_query(sql, id)

    

def getReview(id: int) -> Review:
    sql = "select * from Reviews where reviewID = ?"
    res = fetch_query(sql, id)
    review = Review()
    review.__init__(res[0], res[1], res[2], res[3], res[4])