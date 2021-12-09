from flask import Blueprint, render_template
from flask_login import current_user

bp = Blueprint("new_recipe", __name__)


@bp.route("/new_recipe")
def new_recipe():
    """
        Create a blueprint to display a new recipe page.
    """
    return render_template("new_recipe.html", user=current_user)
