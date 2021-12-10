from flask import Blueprint, render_template, redirect
from flask.json import jsonify
from werkzeug.wrappers import StreamOnlyMixin
from flask_login import current_user
from ..models import (
    db,
    User
)

bp = Blueprint("manage", __name__)


@bp.route("/manage")
def new_recipe():
    """
        Create a blueprint to display a manage page.
    """
    if not current_user.is_anonymous:
        uid = current_user.get_id()
        # Check if user is manager
        userDetails = User.query.filter(uid == User.uid).first()
        if userDetails.is_manager:
            return render_template("manage.html", user=current_user)
        else:
            return redirect("/")
    else:
        return redirect("/")
