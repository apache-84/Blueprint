import sqlite3

DB_FILE = "csci375team3.db"

def insert():
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.executemany("""
                INSERT INTO Courses (courseID, courseName, description, recommendHours)
                """
        )
        