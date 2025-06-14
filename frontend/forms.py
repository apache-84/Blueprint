# Forms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField, RadioField, FloatField
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[
        DataRequired(), 
        Length(min=2, max=20)])
    password = PasswordField("Password", validators=[
        DataRequired(), 
        Length(min=2)])
    userType = RadioField("User Type", choices=[
        ("S", "Student"), 
        ("F", "Faculty")], 
        validators=[DataRequired()])
    remember = BooleanField("Remember me", default=False)
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[
        DataRequired(), 
        Length(min=2, max=20)])
    userType = RadioField("User Type", choices=[
        ("S", "Student"), 
        ("F", "Faculty")], 
        validators=[DataRequired()])
    password = PasswordField("Password", validators=[
        DataRequired(), 
        Length(min=2)])
    password2 = PasswordField("Repeat Password", validators=[
        DataRequired(), 
        EqualTo('password', message='Passwords must match.')])
    submit = SubmitField("Register Account")

class ReviewForm(FlaskForm):
    difficulty = FloatField('Difficulty:', validators=[ 
        DataRequired(),
        NumberRange(min=0.0, max=5.0, message="Difficulty must be between 0.0 and 5.0.")
    ])
    hours = FloatField('Recommended hours per week to be successful in this course:', validators=[ 
        DataRequired(),
        NumberRange(min = 1.0, message="Value must be greater than 1.0.")
    ])
    title = StringField("Title", validators=[
        DataRequired(),
        Length(max=50)])
    text = TextAreaField("Enter the text for your review:", validators=[Length(max=500, message="Reviews must be 500 characters or less.")])
    submit = SubmitField("Post Review")
