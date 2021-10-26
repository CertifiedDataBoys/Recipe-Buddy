from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp



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


    username = StringField("Username",
        validators=[
            DataRequired(),
            Length(max=32,
                   message="Usernames can be no more than 32 characters long!"
            )
        ]
    )
    email = StringField("Email",
        validators=[
            DataRequired(), Email(),
            Length(max=64,
                   message="Emails can be no more than 64 characters long!"
            )
        ]
    )
    confirm_email = StringField("Repeat email",
        validators=[
            DataRequired(),
            EqualTo("email", message="Emails must match!"),
        ]
    )
    password = PasswordField("Password",
        validators=[
            DataRequired(),
            Length(min=8, message="Password must be at least 8 \
                                   characters long!"
            ),
            Regexp(r"^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?\W).*$",
                   message="Password must have at least one uppercase \
                            character, lowercase character, digit, and \
                            special character."
            )
        ]
    )
    confirm_password = PasswordField("Repeat password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match!"),
        ]
    )
    submit = SubmitField("Register")
