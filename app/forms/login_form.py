from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
    """
        This Form handles user logins using a username and password

        Attributes:
            username (StringField):
                        Input for a username
            password (PasswordField):
                        Input for a user's password
            remember_me (BooleanField):
                        Input to remember if a user is logged in to a browser
            submit (SubmitField):
                        Button to submit all fields to Recipe Buddy
    """


    username  = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField("Remember me?", default=True)
    submit = SubmitField('Log In')
