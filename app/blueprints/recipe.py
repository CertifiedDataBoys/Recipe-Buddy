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


    ingredients_query = db.session.query(Ingredient, IngredientInRecipe) \
        .join(IngredientInRecipe, IngredientInRecipe.recipe_key == recipe.pk) \
        .filter(Ingredient.pk == IngredientInRecipe.ingredient_key) \
        .all()

    ingredients = []

    for i in ingredients_query:

        ingredient = i[0]
        ingredient_in_recipe = i[1]

        unit = ""
        if ingredient_in_recipe.count == 1:
            unit = ingredient.unit_of_measure
        else:
            unit = ingredient.units_plural

        ingredients.append([
            ingredient_in_recipe.count,
            unit,
            ingredient.name,
            ingredient_in_recipe.optional
        ])

    return render_template("recipe.html", recipe=recipe_json, user=user_json,
                           ingredients_list=ingredients)
