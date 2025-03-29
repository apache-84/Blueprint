from Course import Course
from Review import Review
from CourseData import writeReview, getCourse  #for writeReview function,getCourse for semesterData

class Student():
    def __init__(self, stuID: int = 0, username: str = "", password: str = ""):
        """
        Instantiates a Student user object with the given values: stuID, username, and password (hashed). Otherwise, will use default values.

        :param stuID: The student's unique ID.
        :param username: The student's account username.
        :param pssword: The student's encrypted password.
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

    # Setter methods:
    def setID(self, sid: str):
        self.__stuID = sid

    def setUsername(self, user: str):
        self.__username = user
    
    def setPassword(self, pWord: int):
        self.__password = pWord

    def encryptPassword(self, password: str = ""):
        pass

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
        
        semesterData[1] = dsum / len(selectedCourses)
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
            
            
        