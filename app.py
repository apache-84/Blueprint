from backend.Announcement import *
from backend.AnnouncementData import *
from backend.Review import *
from backend.ReviewData import *
from backend.Course import *
from backend.CourseData import *
from backend.Student import *
from backend.StudentData import *
from backend.Faculty import *
from backend.FacultyData import *
from backend.CoursesTaughtData import *
from backend.UserData import *
from database.db_setup import *
from frontend.forms import *
from flask import Flask, render_template, request, url_for, redirect, session, flash
from datetime import datetime


app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend/static')

app.config["SECRET_KEY"] = "secretkeyoooooo"

DB_FILE = "database/blueprintdb.db"

@app.route('/', methods=["GET", "POST"])
def index():
    print("Session:", dict(session))
    # Get every available course
    courseData = []
    for c in getAllCourses():
        courseData.append(courseToDict(c))

    # Get three most recent announcements.
    annBoard = []
    for a in getAnnouncementBoard():
        annBoard.append(annToDict(a))

    return render_template("index.html", courses = courseData, announcementBoard = annBoard)


@app.route('/register', methods=["GET", "POST"])
def register():

    registerForm = RegistrationForm()

    if registerForm.validate_on_submit(): #we want a way to check if s or f called to insert for faculty or student query
        try:
            username = registerForm.username.data
            password = registerForm.password.data
            userType = registerForm.userType.data 

            registerUser(userType, username, password)
            flash(f"Registration for {username} successful!", "success")
            return redirect(url_for("index"))  # Change back to home page
        except UsernameTakenError as e: 
            registerForm.username.errors.append(str(e))

    return render_template("register.html", registerForm = registerForm)

@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        try:
            userType = loginForm.userType.data
            username = loginForm.username.data
            password = loginForm.password.data

            loginUser(userType, username, password)
            flash(f"Login for {username} successful!", "success")

            if loginForm.remember.data == True:
                session.permanent = True
            else:
                session.permanent = False

            return redirect(url_for('index'))
        except UsernameNotFoundError as e:
            loginForm.username.errors.append(str(e))
        except IncorrectPasswordError as e:
            loginForm.password.errors.append(str(e))
    
    return render_template("login.html", loginForm = loginForm)

@app.route('/list_users', methods=['GET'])
def list_users():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()

    cursor.execute("SELECT * FROM FacultyMembers")
    faculty = cursor.fetchall()

    conn.close()

    return render_template("list_users.html", students=students, faculty=faculty)

@app.route('/courses/<cid>', methods=['GET', 'POST'])
def courses(cid):
    # Replacing hyphens from passed URL back to spaces for DB querying.
    cid = cid.replace("-", " ")
    
    # Get the course from cid as a dict.
    c = getCourse(cid)
    course = courseToDict(c)

    # Get all course reviews
    reviews = []
    reviewList = getReviewData(cid)
    for r in reviewList:
        reviews.append(reviewToDict(r))


    # Get current student's review
    stuReview = None
    if session.get('userType') == "S":
        stuReview = getStuReview(session.get('userID'), cid)
        # If a stu review exists, get it as a dict and remove it from the rest of the reviews.
        if stuReview != None:
            for index, review in enumerate(reviews):
                if review['id'] == stuReview.getID():
                    stuReview = reviews.pop(index)
                    break

    # Get all course announcements
    announcements = []
    annList = getCourseAnnouncements(cid)
    for a in annList:
        announcements.append(annToDict(a))

    return render_template("course.html", course=course, reviews=reviews, announcements=announcements, stuReview = stuReview)

@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")

@app.route('/help', methods=['GET'])
def help():
    return render_template("help.html")

@app.route('/calculator', methods=['GET'])
def calculator():
    courses = []
    semesterData = []

    # Initialize selected courses incase it doesn't exist.
    initSelectedCourses()

    # Get all course dicts for course cards
    for cid in session.get('selected_courses'):
        courses.append(courseToDict(getCourse(cid)))

    if 'semester_data' in session:
        semesterData = session.pop('semester_data')

    print(courses)

    return render_template("calculator.html", courses = courses, semesterData = semesterData)
    

@app.route('/semester/process', methods=['POST'])
def calculateSemester():
    # Initialize selected courses incase it doesn't exist.
    initSelectedCourses()

    # Get all course IDs to calculate semester\
    courseIDs = session.get('selected_courses')

    session['semester_data'] = calculateSemesterData(courseIDs)

    return redirect(url_for('calculator'))

@app.route('/semester/clear', methods=['POST'])
def clearSemester():
    # Initialize selected courses incase it doesn't exist.

    session['selected_courses'] = []

    return redirect(url_for('calculator'))

# Route to add course to a student's selected courses.
@app.route('/add-course/<cid>', methods=['POST'])
def addCourse(cid):
    # Replacing hyphens from passed URL back to spaces for DB querying.
    cid = cid.replace("-", " ")

    # Initialize selected courses incase it doesn't exist.
    initSelectedCourses()

    try:
        selectCourse(cid)
    except SelectCourseError as e:
        print(str(e))
    
    flash(f"{cid} added to your semester!")

    # Will return back to page user visited this route from, or index if they accessed it directly.
    return redirect(request.referrer or url_for('index'))

# Route to remove course from a student's selected courses.
@app.route('/remove-course/<cid>', methods=['POST'])
def removeCourse(cid):
    # Replacing hyphens from passed URL back to spaces for DB querying.
    cid = cid.replace("-", " ")

    # Initialize selected courses incase it doesn't exist.
    initSelectedCourses()

    print("Selected Courses:", session.get('selected_courses'))

    try:
        session['selected_courses'].remove(cid)
        session['selected_courses'] = session['selected_courses']
    except Exception as e:
        print(str(e))
    
    print("Selected Courses:", session.get('selected_courses'))


    flash(f"{cid} removed from your semester!")

    # Will return back to page user visited this route from, or index if they accessed it directly.
    return redirect(request.referrer or url_for('index'))


@app.route('/logout')
def logout():
    session.clear()
    session['userType'] = "G"
    session['username'] = ""
    session['userID'] = ""
    flash("You have logged out!")
    return redirect(url_for('index'))

@app.route('/reviews/<int:stuID>')
def reviews(stuID: int):
    # Sanity check, should never need this.
    if session.get('userType') != "S":
        flash("You must be a student to have posted reviews.")

    reviews = []
    stuReviews = getReviews(stuID)
    for review in stuReviews:
        reviews.append(reviewToDict(review))

    return render_template('your_reviews.html', reviews = reviews)

@app.route('/courses/<cid>/make-review', methods=['GET', 'POST'])
def makeReview(cid):
    # Sanity check, shouldn't need
    if session.get('userType') != "S":
        flash("Only students can write reviews. You are not a registered student.")
        return redirect(url_for('courses', cid = cid))
    
    editFlag = False # Since we are making and not editing a review.
    reviewForm = ReviewForm()

    if reviewForm.validate_on_submit():
        difficulty = reviewForm.difficulty.data
        hours = reviewForm.hours.data
        title = reviewForm.title.data
        text = reviewForm.text.data
        r = Review(text=text, diff=difficulty, hours=hours)
        return redirect(url_for('reviews', session.get('userID')))
    
    return render_template("review_form.html", form = reviewForm, cid = cid, editFlag = editFlag)
@app.route('/courses/<cid>/edit-review', methods=['GET', 'POST'])
def editReview(cid):
    # Sanity check, shouldn't need
    if session.get('userType') != "S":
        flash("Only students can edit reviews. You are not a registered student.")
        return redirect(request.referrer or url_for('index'))
    
    cid = cid.replace("-", " ")
    editFlag = True # Since we are editing and not making a review.

    reviewForm = ReviewForm()
    # Get the review
    review = getStuReview(session.get('userID'), cid)


    # When getting the page.
    if request.method == 'GET':        
        reviewForm.difficulty.data = review.getDifficulty()
        reviewForm.hours.data = review.getHours()
        # reviewForm.title.data = review.getTitle()
        reviewForm.text.data = review.getText()
        lastUpdated = review.getDate()

    if reviewForm.validate_on_submit():
        review.setDifficulty(reviewForm.difficulty.data)
        review.setHours(reviewForm.hours.data)
        # review.setTitle(reviewForm.title.data)
        review.setText(reviewForm.text.data)
        review.setDate(str(datetime.today().date()))

        updateReview(review, session.get('userID'))

        return redirect(url_for('reviews', session.get('userID')))
    return render_template("review_form.html", form = reviewForm, lastUpdated = lastUpdated, cid = cid, reviewID = review.getID(), editFlag = editFlag)


@app.route('/delete-review/<int:reviewID>', methods=['GET'])
def deleteReview(reviewID):
    # Sanity check, shouldn't need
    if session.get('userType') != "S":
        flash("Only students can edit reviews. You are not a registered student.")
        return redirect(request.referrer or url_for('index'))
    
    # If review exists, delete it.
    if getReview(reviewID) != None:
        deleteReviewDB(reviewID)
    else:
        flash("You have not written a review for this course. Can't delete review.")
    
    return redirect(url_for('reviews', stuID = session.get('userID')))



@app.route('/submit-review/<int:stuID>/<cid>')
def submitReview(stuID: int, cid: str, review: Review):
    cid = cid.replace("-", " ")

    writeReview(review, cid, stuID)
    

    return redirect(url_for('courses', cid = cid.replace(" ", "-")))

if __name__ == '__main__':
    app.run(debug=True)
