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
from frontend.forms import RegistrationForm, LoginForm
from flask import Flask, render_template, request, url_for, redirect, session, flash

app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend/static')

app.config["SECRET_KEY"] = "secretkeyoooooo"

# Default user data
# session['userType'] = "G"
# session['username'] = ""
# session['userID'] = ""

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

    # Get all course announcements
    announcements = []
    annList = getCourseAnnouncements(cid)
    for a in annList:
        announcements.append(annToDict(a))

    return render_template("course.html", course=course, reviews=reviews, announcements=announcements)

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

# WIP - Route to add course to a student's selected courses.
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

if __name__ == '__main__':
    app.run(debug=True)
