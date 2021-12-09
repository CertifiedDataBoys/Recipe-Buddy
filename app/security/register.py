from flask import current_app
from ..models import User


def username_exists(username):
    """
        Check if there is a user with the given username

        Arguments:
            username (str):
                        The username we are checking for.

        Returns:
            bool:       True if there is a user with this username,
                        False otherwise.
    """

    return User.query.filter(User.username == username).first() != None


def email_exists(email):
    """
        Check if there is a user with the given email

        Arguments:
            email (str):
                        The email address we are checking for.

        Returns:
            bool:       True if there is a user with this email address,
                        False otherwise.
    """

    return User.query.filter(User.email == email).first() != None


def register_user(db, user):
    """
        Register a User into our database
    """

    with current_app.app_context():

        db.session.add(user)
        db.session.commit()
