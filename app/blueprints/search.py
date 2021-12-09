from flask import Blueprint, render_template
from flask_login import current_user

bp = Blueprint("search", __name__)

@bp.route("/search")
def recipe_search():
    """
        Create a blueprint to display a search page.
    """
    return render_template("search.html", user=current_user)
