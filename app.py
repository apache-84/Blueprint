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
#from frontend.forms import *
from flask import Flask, render_template, request, url_for, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)

app.config["SECRET_KEY"] = "secretkeyoooooo"

#move this later back to forms.py
#class RegistrationForm(FlaskForm):
#    username = StringField("Username", validators=[Length(min=2, max=20)])
#    userType = [("Student", "S"), ("Faculty", "F")]
#    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
#    register = SubmitField("Register Account")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[Length(min=2, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=2)])
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[Length(min=2, max=20)])
    userType = [("Student", "S"), ("Faculty", "F")]
    password = PasswordField("Password", validators=[DataRequired(), Length(min=2)])
    submit = SubmitField("Register Account")


@app.route('/', methods=["GET", "POST"])
def index():
    form = LoginForm()
    return render_template("index.html", form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    registerForm = RegistrationForm()

    if registerForm.validate_on_submit():
        username = registerForm.username.data
        password = registerForm.password.data
        registerForm = registerForm
    return render_template("register.html", registerForm = registerForm)


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        try:
            student = loginStudent(loginForm.username.data, loginForm.password.data)
            session['student_id'] = student.getID()
            session['student_id'] = student.getUsername()
            return redirect(url_for('index'))
        except UsernameNotFoundError as e:
            loginForm.username.errors.append(str(e))
        except IncorrectPasswordError as e:
            loginForm.password.errors.append(str(e))
    
    return render_template("login.html", loginForm = loginForm)



if __name__ == '__main__':
    app.run(debug=True)
