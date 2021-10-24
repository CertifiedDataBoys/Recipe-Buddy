from ..models import User
import flask_login


login_manager = flask_login.LoginManager()


@login_manager.user_loader
def load_user(uid):
    """
        user_loader function required by Flask-Login.

        Args:
            uid (int):
                        User ID
    """
    return User.query.get(int(uid))
