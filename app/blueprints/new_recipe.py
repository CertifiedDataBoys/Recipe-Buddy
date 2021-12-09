from flask import Blueprint, render_template, redirect
from flask_login import current_user

bp = Blueprint("new_recipe", __name__)


@bp.route("/new_recipe")
def new_recipe():
    """
        Create a blueprint to display a new recipe page.
    """
    if not current_user.is_anonymous:
        return render_template("new_recipe.html", user=current_user)
    else:
        return redirect("/login", code=302)
