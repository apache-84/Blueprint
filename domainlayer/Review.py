from datetime import datetime

class Review():
    def __init__(self, id: int = 0, text: str = "", diff: float = 0.0, hours: int = 0, date: str = ""):
       self.__reviewID = id
       self.__reviewText = text
       self.__difficulty = diff
       self.__recHours = hours
       self.__reviewDate = date
    
    def getID(self) -> int:
        return self.__reviewID
    
    def getText(self) -> str:
        return self.__reviewText

    def getDifficulty(self) -> float:
        return self.__difficulty

    def getHours(self) -> int:
        return self.__recHours
    
    def getDate(self) -> str:
        return self.__reviewDate

    def setID(self, id):
        self.__reviewID = id

    def setText(self, text):
        self.__reviewText = text

    def setDifficulty(self, diff):
        self.__difficulty = diff
    
    def setHours(self, hours):
        self.__recHours = hours
    
    def setDate(self, date):
        self.__reviewDate = date
        
    def createReview(self):
        # Get difficulty section
        while True:
            try:
                diff = float(input("Enter a difficulty: "))
                if (diff >= 0.0 and diff <= 5.0):
                    self.setDifficulty(diff)
                    break
                else:
                    print("Invalid input: Difficulty must be between 0.0 and 5.0.")
            except ValueError:
                print("Value is of incorrect data type, try again.")
        
        # Get hours section
        while True:
            try:
                hours = int(input("Enter the recommended hours per week someone should spend on this course: "))
                if (hours > 0):
                    self.setHours(hours)
                    break
                else:
                    print("Invalid input: Hours cannot be negative.")
            except ValueError:
                print("Value is of incorrect data type, try again.")
        
        # Get Text Section
        while True:
            text = str(input("Enter text for your review: \n"))
            if (len(text) > 0 and len(text) <= 500):
                self.setText(text)
                break
            else:
                print("Text is an invalid character size, must be between 0 and 500 characters.")
        
        # Set the date to current day
        self.setDate(str(datetime.today().date()))
        
        print("Writing review to database...")


if __name__ == '__main__':
    r = Review()
    r.createReview()
    print("Difficulty:", r.getDifficulty(), "\nRecommended Hours:", r.getHours(), "\nReview Text:\n", r.getText(), "\nDate:", r.getDate())
    
    