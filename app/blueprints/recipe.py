from flask import abort, Blueprint, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from ..models import db, User, Ingredient, Recipe, IngredientInRecipe
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

    # The test recipe is the recipe where recipe.pk = 1
    recipe_query_url = (
        "http://localhost:" + port
        + url_for("api_v1_recipes.get_single_recipe")
        + "?pk={0}".format(pk)
    )
    recipe_query_json = urllib.request.urlopen(recipe_query_url).read()
    recipe_json = json.loads(recipe_query_json)["recipe"]

    # Did our recipe query return anything?
    if not recipe_json:
        return abort(404)


    return render_template("recipe.html", pk=pk)
