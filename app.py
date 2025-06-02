from backend import *
#from frontend.forms import *
from flask import Flask, render_template, request
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
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    login = SubmitField("Login")

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[Length(min=2, max=20)])
    userType = [("Student", "S"), ("Faculty", "F")]
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    register = SubmitField("Register Account")


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

if __name__ == '__main__':
    app.run(debug=True)
