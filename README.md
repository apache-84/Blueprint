# Blueprint
GitHub repo for our CSCI 375 project, Blueprint!

## Introduction / Use of the product
Blueprint is a system designed to help VIU CS students balance their semesters by avoiding semesters full of difficult courses and semesters full of easy courses. Blueprint relies on collecting data from past students to determine the time/workload needed for each course. Future students will have the ability to balance/review upcoming semesters to design a university career with consistency and reliability.
- Students can add courses to their semester and calculate their semester data, where our system will give them feedback based on the courses they've selected for a semester. 
- Students can write reviews for courses they have taken and leave their own difficulty rating, etc. 
- Students can give feedback to faculty directly through reacting to announcements of proposed or made changes to courses.

This system is also designed to help the VIU CS faculty better balance the program's courses and schedule! Teachers and faculty often forget what it’s like to be a beginner and don’t know what is too little or too much content for a course. Faculty can add courses, edit existing courses, make announcements for changes of courses, and view student review data!

## Directory Structure

There are three directories in this repository:
- **Database**: This directory contains the SQLite database file, and a Python script that inserts dummy data into the database.
- **Application**: This directory is the main directory of the system. This is the directory you want to be in to execute Python scripts and to use our system.
- **WebPOC**: The web proof of concept directory is work that was done by our team for the web frontend. These components have not been integrated with the backend and are completely independent. 
    - Some assets from this folder may be shown in our project demo.

## Key Files
This section describes all of the key files of the repository and what they do.

### Database Directory Key Files
- **blueprintdb.db**: This is our SQLite database file. All of the data for our system is stored in this file. If you want to check the contents of the database (not through methods in our application defined later), you may do so by running the command `sqlite3 ../Database/blueprintdb.db` from the `Application` direcftory. You may then enter any SQL queries you desire.
- **FillData.py**: This is the Python script that inserts dummy data into the database (**if the database is empty**, otherwise it will cause an error). 
    - **IMPORTANT**: Run this file 1. Right after running `db_setup.py` from the `Application` directory and 2. Run the file by typing `python3 ../Database/FillData.py` from the `Application` directory.

### Application Directory Key Files
- **main.py**: This is the main routine for our system. To use our system, run this file by typing the command `python3 main.py` from the `Application` directory.
    - If you are on Windows, use the command `py main.py` instead. 
- **db_setup.py**: This is the database initialization file. At the moment, this file will drop all tables and then recreate all of them, which means it will **wipe the database and initialize it with no records**.
    - If you wish to wipe the database, run this file by typing `python3 db_setup.py` from the `Application` directory. If you want to populate the database with dummy data, type `python3 ../Database/FillData.py` after initializing the database.
    - If you wish to just create the tables and not drop them, comment out **line 130** of `db_setup.py`. If you wish to just drop the tables from the database and not reinitialize them, comment out **line 131** of `db_setup.py`. 

## Set up and run the prototype
Note: No Python packages are needed for the set up process of running our system. Therefore, no virtual environment setups or package installations are required.

1. To run our system, you must first be in the `Application` directory. Without being in the `Application` directory, nothing will work.
2. Run `db_setup.py`  in the `Application` directory if you do not see a file named `blueprintdb.db` in the `Database` directory.
3. If you want to have dummy data filled into the database, run `FillData.py` from the `Application` directory (follow instructions for file above).
4. To run the system, type `python3 main.py` from the `Application` directory if you are on a Linux machine. If you are on a Windows machine, type `py main.py`.
5. Once you are in our system, you will be greeted. Follow the instructions on the terimnal to use our system. Enjoy!

## Troubleshooting
Here are some tips for troubleshooting if something comes up:
1. If the system runs into an error or crashes unexpectedly, an error message should appear in the terminal. Look at the error message and see whether or not you can determine what type of operation could be causing the error (memory, database, infinite loop, incorrect data types, etc.)
2. Likely, the database or the data layer functions are causing the error. To fix database related issues, do steps 2 and 3 in the 'set up' section. 
    - Note that this will mean all new data you have inputted in the system will be gone and you will need to reinput it again.
3. Sometimes the program crashes unexpectedly because there are a lot of objects and memory locations flying around in the system, meaning just changing nothing and running `main.py` again can solve some issues.

## Known Issues
Here is a list of issues with the system known by the development team:
- The occassional unexpected crash occurs when running the system. No consistency in what causes the crash has been found, nor are the crashes common.

Here is a list of functionalities/requirements our system promised in the requirements and does not provide at the moment:
- The ability to verify users' identities through external single sign-on on the VIU student record website.
- Moderation of reviews to prevent hateful speech from being posted.
- The ability to filter courses by attribute/name from the list of all courses.
- The semester a student makes being able to be exported as a schedule.
- The badge reward for students who review courses often.
- Guidelines for writing reviews and course information.
- Ensuring that in order to write a review, student must have taken that course before.
- Updating live servers to HTML5 on any supported browser.
- Presenting course information to students through flashcards.