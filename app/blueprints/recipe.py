from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from ..models import db, User, Ingredient, Recipe, IngredientInRecipe


bp = Blueprint("test", __name__)


@bp.route("/recipe/<pk>")
def recipe(pk="0"):
    """
        Create a blueprint to display a test page.
        This should only display the recipe with the primary key of 1.
        For testing, this is a BLT sandwich.
    """


    # The test recipe is the recipe where recipe.pk = 1
    recipe_query = db.session.query(Recipe, User) \
        .join(User, User.uid == Recipe.uploaded_by) \
        .filter(Recipe.pk == pk) \
        .first()

    # Did our recipe query return anything?
    if not recipe_query:
        return render_template("404.html")

    recipe = recipe_query[0]
    user = recipe_query[1]

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

    return render_template("recipe.html", recipe=recipe, user=user,
                           ingredients_list=ingredients)
