from datetime import datetime
from flask import Blueprint, jsonify, request
from ...models import (
    db,
    Recipe,
    RecipeComment,
    User
)
import re


bp = Blueprint("api_v1_interactions", __name__)


@bp.route("/api/v1.0.0/public/recipe/get_single_comment")
def get_single_comment():
    """
        Create a blueprint to get a single comment as a JSON file.
        This takes in a comment's primary key (?pk=<...>).
    """


    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify([])


    query = RecipeComment.query.filter(RecipeComment.pk == key)

    return jsonify(comment = query.first())


@bp.route("/api/v1.0.0/public/recipe/get_comments_in_recipe")
def get_comments_in_recipe():
    """
        Create a blueprint to get all of the comments and the username + uid of
        the user who posted them from a recipe as a JSON file.
        This takes in a recipe's primary key (?pk=<...>).
    """


    key = request.args.get("pk")


    # error handling --- improve later
    if not key:

        return jsonify([])


    recipe_comment_query = (
        db.session.query(RecipeComment)
        .join(User, User.uid == RecipeComment.uid)
        .with_entities(
            RecipeComment.pk, RecipeComment.recipe_key,
            RecipeComment.contents, RecipeComment.uploaded,
            RecipeComment.reply_to, RecipeComment.suggestion,
            RecipeComment.uid, User.username
        )
        .filter(RecipeComment.recipe_key == key)
    )
    recipe_comments = recipe_comment_query.all()
    comments_dict = {
        "comments": [
            {
                "pk": comment.pk,
                "recipe_key": comment.recipe_key,
                "contents": comment.contents,
                "uploaded": comment.uploaded,
                "reply_to": comment.reply_to,
                "suggestion": comment.suggestion,
                "user":
                {
                    "uid": comment.uid,
                    "username": comment.username
                }
            }
            for comment in recipe_comments
        ]
    }

    return jsonify(comments_dict)


@bp.route("/api/v1.0.0/public/recipe/post_recipe_comment",
           methods=["GET", "POST"])
def post_recipe_comment():

    comment = request.json

    # Sanitize contents
    contents = comment["contents"]
    contents = contents.replace("\r\n", "\n")
    contents = contents.replace("\r", "\n")

    db.session.add(
        RecipeComment(
            uid=comment["uid"],
            recipe_key=comment["recipe_key"],
            reply_to=comment["reply_to"],
            contents=contents,
            uploaded=datetime.now(),
            suggestion=comment["suggestion"]
        )
    )
    db.session.commit()

    return jsonify(status="success")
