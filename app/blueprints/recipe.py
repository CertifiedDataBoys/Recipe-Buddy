from flask import abort, Blueprint, render_template, request, url_for
import json
import urllib.request
import os

port = os.getenv('PORT') or "5000"

bp = Blueprint("recipe", __name__)


@bp.route("/recipe/<int:pk>")
def recipe(pk="0"):
    """
        Create a blueprint to display a test page.
        This should only display the recipe with the primary key of 1.
        For testing, this is a BLT sandwich.
    """

    return render_template("recipe.html", pk=pk)
