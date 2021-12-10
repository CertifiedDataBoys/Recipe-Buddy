from flask import Blueprint, render_template, redirect
from flask_login import current_user

bp = Blueprint("manage", __name__)


@bp.route("/manage")
def new_recipe():
    """
        Create a blueprint to display a manage page.
    """
    if not current_user.is_anonymous:
        return render_template("manage.html", user=current_user)
    else:
        return redirect("/login", code=302)
