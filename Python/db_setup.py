# CMON 20250309 CSCI 375 db_setup.py
# Initalizes the database for Blueprint by creating tables
# Run once to create csci375team3.db

import sqlite3

DB_FILE = "csci375team3.db"


def drop_tables():
    """
    FOR TESTING PURPOSES ONLY: Drops all tables in the database so they can be remade if small modifications are needed for tests to work.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS FacultyMembers;")
    cursor.execute("DROP TABLE IF EXISTS Students;")
    cursor.execute("DROP TABLE IF EXISTS Courses;")
    cursor.execute("DROP TABLE IF EXISTS Announcements;")
    cursor.execute("DROP TABLE IF EXISTS Reviews;")
    cursor.execute("DROP TABLE IF EXISTS CourseTaught;")
    cursor.execute("DROP TABLE IF EXISTS CourseEditHistory;")
    cursor.execute("DROP TABLE IF EXISTS AnnouncementReactions;")

    conn.commit()
    conn.close()


def create_tables():
    """
    Initializes all tables in the database, should only be executed one time to create the database file `csci375team3.db`
    """
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
            reviewDate TEXT NOT NULL
        );
    """)
            # courseID TEXT,
            # studentID INTEGER,
            # FOREIGN KEY (courseID) REFERENCES Courses(courseID),
            # FOREIGN KEY (studentID) REFERENCES Students(studentID)
    
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

# note: basic command-line test for table existence: `sqlite3 csci375team3.db ".tables"`
if __name__ == "__main__":
    drop_tables()
    create_tables()
    print("Database initialized. Have a nice day.")