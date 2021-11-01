from .database import db
from flask_login import UserMixin
import hashlib


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

    uid = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    verified = db.Column(db.Boolean, nullable=False)
    password_hash = db.Column(db.String(256), unique=False, nullable=False)

    def _hash(self, password, salt):

        return hashlib.pbkdf2_hmac("sha512",
                                   password.encode(), salt.encode(),
                                   100000, dklen=128).hex()

    def set_password(self, password):

        self.password_hash = self._hash(password, "SaltKBanerjee")

    def check_password(self, password):

        return self.password_hash == self._hash(password, "SaltKBanerjee")

    def get_id(self):

        return str(self.uid)


class UserProfile(db.Model):

    uid = db.Column(db.Integer, db.ForeignKey("user.uid"), primary_key=True)
    favorite_recipe = db.Column(db.Integer, db.ForeignKey("recipe.pk"),
                                nullable=False)
    has_profile_photo = db.Column(db.Boolean, nullable=False)
