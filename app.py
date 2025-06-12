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

DB_FILE = "database/blueprintdb.db"

@app.route('/', methods=["GET", "POST"])
def index():
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
    user_type = registerForm.userType.data

    if registerForm.validate_on_submit(): #we want a way to check if s or f called to insert for faculty or student query
        try:
            username = registerForm.username.data
            password = registerForm.password.data
            user_type = registerForm.userType.data # boolean for student or faculty
            # Make a cookie to store user's ID, name, and type.      
            if user_type == 'S':
                registerStudent(username, password)
                loginUser
                return redirect(url_for("index"))  # Change back to home page
            elif user_type == 'F':
                registerFaculty(username, password)
                return redirect(url_for("index"))  # Change back to home page
        except UsernameTakenError as e: 
            registerForm.username.errors.append(str(e))
        flash(f"Registration for {session['user_name']} successful!")

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
            loginUser(userType, loginForm.username.data, loginForm.password.data)
            flash("Login successful!")

            if loginForm.remember_me.data:
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
    pass

# WIP - Route to add course to a student's selected courses.
@app.route('/add-course/<cid>', methods=['POST'])
def addCourse(cid):
    # Replacing hyphens from passed URL back to spaces for DB querying.
    cid = cid.replace("-", " ")

    # Check if logged in as a student
    if session['user_type'] != "S":
        raise NotAStudentError("You must be logged in as a student user to add courses to your semester.")
    

    s = Student(session['user_id'])

    try:
        s.selectCourse(cid)
        print("Selected Courses:")
        for c in s.selectedCourses:
            print(c.getID())
    except SelectCourseError as e:
        print(str(e))
    
    return redirect(url_for('courses' , cid=cid.replace(" ", "-")))

if __name__ == '__main__':
    app.run(debug=True)
