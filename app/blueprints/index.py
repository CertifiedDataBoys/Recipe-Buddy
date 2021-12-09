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

@bp.route("/search")
def recipe_search():
    """
        Create a blueprint to display a search page.
    """
    return render_template("search.html", user=current_user)

@bp.route("/new_recipe")
def new_recipe():
    """
        Create a blueprint to display a new recipe page.
    """
    return render_template("new_recipe.html", user=current_user)
