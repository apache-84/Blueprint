# Forms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=2)])
    userType = RadioField("User Type", choices=[("S", "Student"), ("F", "Faculty")], validators=[DataRequired()])
    remember = BooleanField("Remember me", default=False)
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    userType = RadioField("User Type", choices=[("S", "Student"), ("F", "Faculty")], validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=2)])
    password2 = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
    submit = SubmitField("Register Account")