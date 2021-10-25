from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired



class RegisterForm(FlaskForm):
    """
        This Form handles user registration using a username, email, and
            password.

        Attributes:
            username (StringField):
                        Input for a username
            email (StringField):
                        Input for a user's email
            password (PasswordField):
                        Input for a user's password
            submit (SubmitField):
                        Button to submit all fields to Recipe Buddy
    """


    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')
