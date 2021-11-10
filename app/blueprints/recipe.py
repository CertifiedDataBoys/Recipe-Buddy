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
    print(recipe_query_url, flush=True)
    recipe_query_json = urllib.request.urlopen(recipe_query_url).read()
    recipe_json = json.loads(recipe_query_json)["recipe"]

    # Did our recipe query return anything?
    if not recipe_json:
        return abort(404)

    user_query_url = (
        "http://localhost:" + port
        + url_for("api_v1_users.get_single_user")
        + "?uid={0}".format(recipe_json["uploaded_by"])
    )
    print(user_query_url, flush=True)
    user_query_json = urllib.request.urlopen(user_query_url).read()
    user_json = json.loads(user_query_json)["user"]

    recipe_instructions_query_url = (
        "http://localhost:" + port
        + url_for("api_v1_recipes.recipe_instructions")
        + "?pk={0}".format(pk)
    )
    print(recipe_instructions_query_url, flush=True)
    recipe_instructions_query_json = urllib.request \
        .urlopen(recipe_instructions_query_url) \
        .read()
    recipe_instructions_json = json.loads(
        recipe_instructions_query_json)["instructions"]
    recipe_instructions_json = sorted(
        recipe_instructions_json,
        key=lambda col: col["instruction_number"]
    )

    recipe_ingredients_query_url = (
        "http://localhost:" + port
        + url_for("api_v1_recipes.recipe_ingredients")
        + "?pk={0}".format(pk)
    )
    print(recipe_ingredients_query_url, flush=True)
    recipe_ingredients_query_json = urllib.request \
        .urlopen(recipe_ingredients_query_url) \
        .read()
    recipe_ingredients_json = json.loads(
        recipe_ingredients_query_json)["ingredients"]

    ingredients = []

    for ingredient in recipe_ingredients_json:

        ingredient_pk = ingredient["pk"]
        ingredient_query_url = (
            "http://localhost:" + port
            + url_for("api_v1_food.get_ingredient")
            + "?pk={0}".format(ingredient_pk)
        )
        print(ingredient_query_url, flush=True)
        ingredient_query_json = urllib.request \
            .urlopen(ingredient_query_url) \
            .read()
        ingredient_query_json = json.loads(ingredient_query_json)["ingredient"]

        unit = ""
        if ingredient["count"] == 1:
            unit = ingredient_query_json["unit_of_measure"]
        else:
            unit = ingredient_query_json["units_plural"]

        ingredients.append([
            ingredient["count"],
            unit,
            ingredient_query_json["name"],
            ingredient["optional"]
        ])

    return render_template("recipe.html", pk=pk)
