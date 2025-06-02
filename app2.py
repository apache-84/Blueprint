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

from frontend.forms import *
from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)

app.config["SECRET_KEY"] = "secretkeyoooooo"

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            student = loginStudent(form.username.data, form.password.data)
            session['student_id'] = student.getID()
            session['student_id'] = student.getUsername()
            return redirect(url_for('index'))
        except UsernameNotFoundError as e:
            form.username.errors.append(str(e))
        except IncorrectPasswordError as e:
            form.password.errors.append(str(e))
    
    return render_template("login.html", form=form)
