from flask import Blueprint, render_template
import os

bp = Blueprint("index", __name__)

@bp.route("/")
def index():
    """
        Create a blueprint to display an index page.
        At the moment, this is only a simple test page that displays
            database credentials.
    """

    return render_template("index.html", os=os)
