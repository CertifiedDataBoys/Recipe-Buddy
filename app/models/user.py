from .database import db
from dataclasses import dataclass
from flask_login import UserMixin
import hashlib


@dataclass
class User(UserMixin, db.Model):
    """
        This model represents a Recipe Buddy user.

        Attributes:
            uid (db.Integer):
                        Unique user ID. This is our primary key
            username (db.String(32)):
                        A user's unique username
            email (db.String(64)):
                        A user's unique email
            verified (db.Boolean):
                        Boolean representing if this user is verified or not
            password_hash (db.String(256)):
                        The hash of a user's password
    """

    uid: int
    username: str
    email: str
    verified: bool
    password_hash: str

    uid = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    verified = db.Column(db.Boolean, nullable=False)
    password_hash = db.Column(db.String(256), unique=False, nullable=False)

    def _hash(self, password, salt):
        """
            This function hashes a given password using a given salt. <br>
            Passwords are hased with the <i>SHA512</i> algorithm within
                <i>PBKDF2</i>. The hashes are 256 characters long, and
                <i>PBKDF2</i> is run with 100,000 iterations.

            Args:
                password (str):
                        The user's unhashed password.
                salt (str):
                        The salt we are using for our hash.
        """

        return hashlib.pbkdf2_hmac("sha512",
                                   password.encode(), salt.encode(),
                                   100000, dklen=128).hex()

    def set_password(self, password):
        """
            This function sets the user's password hash based on a given
                unhashed password.

            Args:
                password (str):
                        The user's unhashed password.
        """

        self.password_hash = self._hash(password, "SaltKBanerjee")

    def check_password(self, password):
        """
            This function compares the user's password to a given password.

            Args:
                password (str):
                        An unhashed password to check against.
        """

        return self.password_hash == self._hash(password, "SaltKBanerjee")

    def get_id(self):
        """
            This function returns the uid for this model's user.
        """

        return str(self.uid)


@dataclass
class UserProfile(db.Model):
    """
        This model represents a Recipe Buddy user's profile

        Attributes:
            uid (db.Integer):
                        A foreign key pointing to user.uid. This is the
                            user whose profile we are representing.
            favorite_recipe (db.Integer):
                        A foreign key pointing to recipe.pk. This is the
                            given user's favorite recipe.
            has_profile_photo (db.Boolean):
                        A boolean representing whether or not this user has
                            set their profile photo.
    """

    uid: int
    favorite_recipe: int
    has_profile_photo: bool

    uid = db.Column(db.Integer, db.ForeignKey("user.uid"), primary_key=True)
    favorite_recipe = db.Column(db.Integer, db.ForeignKey("recipe.pk"),
                                nullable=False)
    has_profile_photo = db.Column(db.Boolean, nullable=False)
