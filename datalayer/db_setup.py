# CMON 20250309 CSCI 375 db_setup.py
# initalizes the database for Blueprint by creating tables
# run once to create database.db

import sqlite3

DB_FILE = "csci375team3b.db"

def create_tables():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # note: each query here needs its own `cursor.execute()` 
    # for single-line, a single pair of enclosing double quotation marks is fine
    # for multi-line, triplets of double quotation marks is required

    # turn on SQLite FK cacultyt to DROP and re-CREATE (so, it's possible to fix this, just a pita)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS FacultyMembers (
            facultyID INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        );
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            studentID INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        );
    """)

    # note: SQLite uses `REAL` for floats
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Courses (
            courseID TEXT PRIMARY KEY,
            courseName TEXT NOT NULL,
            description TEXT,
            recommendedHours REAL,
            courseDifficulty REAL,
            sections TEXT,
            recommendedYear INTEGER,
            term TEXT
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Announcements (
            announcementID INTEGER PRIMARY KEY,
            announcementText TEXT,
            announcementDate TEXT NOT NULL,
            courseID TEXT,
            facultyID INTEGER,
            FOREIGN KEY (courseID) REFERENCES Courses(courseID),
            FOREIGN KEY (facultyID) REFERENCES FacultyMembers(facultyID)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Reviews (
            reviewID INTEGER PRIMARY KEY,
            reviewText TEXT,
            difficulty REAL NOT NULL,
            recommendedHours INTEGER NOT NULL,
            reviewDate TEXT NOT NULL,
            courseID TEXT,
            studentID INTEGER,
            FOREIGN KEY (courseID) REFERENCES Courses(courseID),
            FOREIGN KEY (studentID) REFERENCES Students(studentID)
        );
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CoursesTaught (
            courseID TEXT,
            facultyID INTEGER,
            PRIMARY KEY (courseID, facultyID),
            FOREIGN KEY (courseID) REFERENCES Courses(courseID),
            FOREIGN KEY (facultyID) REFERENCES FacultyMembers(facultyID)
        );
    """) 
       
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CourseEditHistory (
            courseID TEXT,
            facultyID INTEGER,
            editDate DATE,
            changeDescription TEXT,
            PRIMARY KEY (courseID, facultyID, editDate),
            FOREIGN KEY (courseID) REFERENCES Courses(courseID),
            FOREIGN KEY (facultyID) REFERENCES FacultyMembers(facultyID)
        );
    """) 
             
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS AnmouncementReactions (
            announcementID INTEGER,
            studentID INTEGER,
            reaction INTEGER,
            PRIMARY KEY (announcementID, studentID),
            FOREIGN KEY (announcementID) REFERENCES Announcements(announcementID),
            FOREIGN KEY (studentID) REFERENCES Students(studentID)
        );
    """) 
    
    conn.commit()
    conn.close()

# note: basic command-line test for table existence: `sqlite3 database.db ".tables"`
if __name__ == "__main__":
    create_tables()
    print("Database initialized. Have a nice day.")