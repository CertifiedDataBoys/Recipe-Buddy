from flask import Blueprint, render_template
from flask_login import current_user

bp = Blueprint("profile", __name__)

@bp.route("/profile")
def recipe_search():
    """
        Create a blueprint to display a profile page.
    """
    return render_template("profile.html", user=current_user)
