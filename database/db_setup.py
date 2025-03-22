# CMON 20250309 CSCI 375 db_setup.py
# create and initalize the database
# run once to create database.db

import sqlite3

DB_FILE = "csci375team3b.db"

def create_tables():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # note: each query here needs its own `cursor.execute()` 
    # for single-line, a single pair of enclosing double quotation marks is fine
    # for multi-line, triplets of double quotation marks is required

    # turn on SQLite FK constraints
    cursor.execute("PRAGMA foreign_keys = ON;")
        
    # note: SQLite doesn't really support adding/removing constraints after building the db like this
    # so we gotta be sure our FK/PK and any CHECK constraints (if we end up using them) are in from the get
    # otherwise, we need to DROP and re-CREATE (so, it's possible to fix this, just a pita)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            UserID INTEGER PRIMARY KEY,
            Username TEXT NOT NULL,
            password TEXT NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS FacultyMembers (
            facultyID INTEGER PRIMARY KEY,
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
            facultyID INTEGER,
            FOREIGN KEY (facultyID) REFERENCES FacultyMembers(facultyID)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Announcements (
            announcementID INTEGER PRIMARY KEY,
            announcementText TEXT NOT NULL,
            announcementDate TEXT,
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
            difficulty REAL,
            recommendedHours INTEGER,
            reviewDate TEXT,
            courseID TEXT,
            studentID INTEGER,
            FOREIGN KEY (courseID) REFERENCES Courses(courseID),
            FOREIGN KEY (studentID) REFERENCES Students(UserID)
        );
    """)
    
    conn.commit()
    conn.close()

# note: basic command-line test for table existence: `sqlite3 database.db ".tables"`
if __name__ == "__main__":
    create_tables()
    print("Database initialized. Have a nice day.")