from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from ..models import db, Ingredient, Recipe, IngredientInRecipe


bp = Blueprint("test", __name__)


@bp.route("/test")
def test():

    # The test recipe is the recipe where recipe.pk = 1
    recipe = Recipe.query.filter_by(pk=1).first()
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
            unit = ingredient_in_recipe.unit_of_measure
        else:
            unit = ingredient_in_recipe.units_plural

        ingredients.append([
            ingredient_in_recipe.count,
            unit,
            ingredient.name,
            ingredient_in_recipe.optional
        ])

    return render_template("test.html", recipe=recipe, ingredients_list=ingredients)
