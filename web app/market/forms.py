from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import length, EqualTo, Email, DataRequired
from market.models import User
class RegistrationForm(FlaskForm):

    def validate_username(self, username_to_check):
        User = User.query.filter_by(username=username_to_check).first()
        if User:
            raise ValidationErr('Username already exists! Please try a different username')
    
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check).first()
        if email_address:
            raise ValidationErr('Email Address already exists! Please try a different email address')


    username = StringField(label='User Name:', validators=[length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email( ), DataRequired()])
    password1 = PasswordField(label='Password', validators=[length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')
    