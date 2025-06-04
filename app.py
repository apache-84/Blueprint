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
from database.db_setup import *
#from frontend.forms import *
from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend/static')

app.config["SECRET_KEY"] = "secretkeyoooooo"

DB_FILE = "database/blueprintdb.db"

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[Length(min=2, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=2)])
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[Length(min=2, max=20)])
    userType = RadioField("Registering as", choices=[("S", "Student"), ("F", "Faculty")], validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=2)])
    submit = SubmitField("Register Account")

@app.route('/', methods=["GET", "POST"])
def index():
    form = LoginForm()
    return render_template("index.html", form=form)


@app.route('/register', methods=["GET", "POST"])
def register():

    registerForm = RegistrationForm()
    user_type = registerForm.userType.data

    if registerForm.validate_on_submit(): #we want a way to check if s or f called to insert for faculty or student query
        try:
            username = registerForm.username.data
            password = registerForm.password.data
            user_type = registerForm.userType.data # boolean for student or faculty

            if user_type == "S":
                student = registerStudent(username, password)
                # Make a cookie to store user's ID, name, and type.      
                session['user_id'] = student.getID()
                session['user_name'] = student.getUsername()
                session['user_type'] = "S"
                return redirect(url_for("index"))  # Change back to home page
            elif user_type == "F":
                pass
                # registerFaculty()
            else:
                flash("Invalid user type selected. Please choose Student or Faculty.", "danger")
                return render_template("register.html", registerForm = registerForm)
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
            student = loginStudent(loginForm.username.data, loginForm.password.data)
            session['user_id'] = student.getID()
            session['user_name'] = student.getUsername()
            session['user_type'] = "S"
            return redirect(url_for('index'))
        except UsernameNotFoundError as e:
            loginForm.username.errors.append(str(e))
        except IncorrectPasswordError as e:
            loginForm.password.errors.append(str(e))
    
    return render_template("login.html", loginForm = loginForm)


@app.route('/nav', methods=['GET'])
def navbartest():  
    return render_template("base.html")



if __name__ == '__main__':
    app.run(debug=True)
