from Course import Course
from Review import Review
from CourseData import writeReview, getCourse, checkCourseID  #for writeReview function,getCourse for semesterData

class Student():
    def __init__(self, stuID: int = 0, username: str = "", password: str = ""):
        """
        Instantiates a Student user object with the given values: stuID, username, and password (hashed). Otherwise, will use default values.

        :param stuID: The student's unique ID.
        :param username: The student's account username.
        :param password: The student's encrypted password.
        """
        self.__stuID = stuID
        self.__username = username
        self.__password = password
        self.selectedCourses = []
    
    # Getter methods:
    def getID(self) -> int:
        return self.__stuID
    
    def getUsername(self) -> str:
        return self.__username
        
    def getPassword(self) -> str:
        return self.__password

    def getSelCourses(self) -> list:
        return self.selectedCourses

    # Setter methods:
    def setID(self, stuID: str):
        self.__stuID = stuID

    def setUsername(self, user: str):
        self.__username = user
    
    def setPassword(self, pWord: int):
        self.__password = pWord

    def calculateSemesterData(self):
        """
        Calculates the semester data from a student's selected courses list.
        
        Returns a 3-element list containing the selected courses, average difficulty, and total recommended hours per week.
        Index 0 is a list of Course objects, index 1 is the semester's average difficulty, index 2 is the total hours per week.
        :return: A list of the results in the format described above, named 'semesterData'.
        """
        dsum = 0.0
        semesterData = [[], 0.0, 0.0]

        for course in self.selectedCourses:
            dsum += course.getDifficulty()
            semesterData[2] += course.getHours()
            semesterData[0].append(course)
        
        semesterData[1] = dsum / len(self.selectedCourses)
        return semesterData

    def selectCourse(self): # In final version, cid will be a param
        """
        Selects a course to be stored in selected courses.
        
        Input a courseID, check that the courseID exists and then append the corresponding Course object with the given courseID to selectedCourses.
        """
        cid = input("What course do you want to add to your semester? ").upper()
        if checkCourseID(cid):
            self.selectedCourses.append(getCourse(cid))
        else:
            print("Course doesn't exist within the database! Try again..")

    
    def makeReview(self):
        """
        FOR TESTING PURPOSES ONLY: Allows student to input a course ID and write a review for the course.
        """
        # Get course section
        while True:
            cid = input("What course is this review for (e.g. CSCI 260)? ").upper()

            if checkCourseID(cid):
                break
            else:
                print("Course doesn't exist within the database! Try again..")

        # Make review section
        review = Review()
        if (review.createReview()):
            writeReview(review, cid, self.getID())
                
    def register(self):

        #Get the username
        while True:
            user = input("Enter a username between 1-20 digits: ")
            if len(user) == 0 or len(user) > 20:
                print("Username is not between 1-20, please try again")
            else:
                self.__username = user
                break
                
        while True:
            pWord = input("Enter a password: ")
            if len(pWord) == 0:
                print("Password must be longer than 0 characters!")
            else:
                self.__password = hash(pWord)
                self.getPassword()
                break
      