from flask import (
    abort, Blueprint,
    render_template, redirect, request, url_for
)
from flask_login import current_user
from ..forms import CommentForm
import json
import urllib.request
import os


port = os.getenv('PORT') or "5000"

bp = Blueprint("recipe", __name__)


@bp.route("/recipe/<int:pk>", methods=["GET", "POST"])
def recipe(pk="0"):
    """
        Create a blueprint to display a test page.
        This should only display the recipe with the primary key of 1.
        For testing, this is a BLT sandwich.
    """

    comment_form = CommentForm()

    if comment_form.validate_on_submit():

        comment_request = {
            "uid": current_user.uid,
            "recipe_key": pk,
            "reply_to": None,
            "contents": comment_form.contents.data,
            "suggestion": False
        }

        req = urllib.request.Request(
            request.host_url + url_for('api_v1_interactions.post_recipe_comment'),
            method="POST"
        )
        req.add_header('Content-Type', 'application/json')
        resp = urllib.request.urlopen(
            req, data=json.dumps(comment_request).encode()
        )

        return redirect(url_for('recipe.recipe', pk=pk))

    return render_template("recipe.html", pk=pk, form=comment_form)
