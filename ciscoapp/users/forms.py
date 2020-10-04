from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField
from wtforms.validators import InputRequired, DataRequired, Length, Email, EqualTo, IPAddress, ValidationError
from ciscoapp.models import User

class LoginForm(FlaskForm):
    username = StringField("Username", validators= [DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField('Login')
    
class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    name = StringField('Name',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')