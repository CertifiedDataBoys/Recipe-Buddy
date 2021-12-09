from flask import Blueprint, render_template
from flask_login import current_user

bp = Blueprint("index", __name__)


@bp.route("/")
def index():
    """
        Create a blueprint to display an index page.
        At the moment, this is only a simple test page that displays
            database credentials.
    """
    return render_template("index.html", user=current_user)
