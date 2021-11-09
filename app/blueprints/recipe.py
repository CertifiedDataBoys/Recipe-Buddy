from flask import abort, Blueprint, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from ..models import db, User, Ingredient, Recipe, IngredientInRecipe
import json
import urllib.request


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
        request.url_root
        + url_for("api_v1_recipes.get_single_recipe")
        + "?pk={0}".format(pk)
    )
    recipe_query_json = urllib.request.urlopen(recipe_query_url).read()
    recipe_json = json.loads(recipe_query_json)["recipe"]

    # Did our recipe query return anything?
    if not recipe_json:
        return abort(404)

    user_query_url = (
        request.url_root
        + url_for("api_v1_users.get_single_user")
        + "?uid={0}".format(recipe_json["uploaded_by"])
    )
    user_query_json = urllib.request.urlopen(user_query_url).read()
    user_json = json.loads(user_query_json)["user"]

    recipe_instructions_query_url = (
        request.url_root
        + url_for("api_v1_recipes.recipe_instructions")
        + "?pk={0}".format(pk)
    )
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
        request.url_root
        + url_for("api_v1_recipes.recipe_ingredients")
        + "?pk={0}".format(pk)
    )
    recipe_ingredients_query_json = urllib.request \
        .urlopen(recipe_ingredients_query_url) \
        .read()
    recipe_ingredients_json = json.loads(
        recipe_ingredients_query_json)["ingredients"]

    ingredients = []

    for ingredient in recipe_ingredients_json:

        ingredient_pk = ingredient["pk"]
        ingredient_query_url = (
            request.url_root
            + url_for("api_v1_food.get_ingredient")
            + "?pk={0}".format(ingredient_pk)
        )
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

    return render_template("recipe.html", recipe=recipe_json, user=user_json,
                           ingredients_list=ingredients,
                           instructions_list=recipe_instructions_json,
                           pk=pk)
