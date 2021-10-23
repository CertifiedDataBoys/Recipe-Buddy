from ..models import Ingredient, Recipe, IngredientInRecipe
from datetime import datetime


def drop_db_tables(app, db):

    with app.app_context():

        IngredientInRecipe.__table__.drop(db.engine)
        Ingredient.__table__.drop(db.engine)
        Recipe.__table__.drop(db.engine)
        db.session.commit()


def create_db_tables(app, db):

    with app.app_context():

        db.create_all()
        db.session.commit()


def create_db_test_data(app, db):

    with app.app_context():

        ingredients = [
            Ingredient(pk=1, name="Bread"),
            Ingredient(pk=2, name="Bacon"),
            Ingredient(pk=3, name="Lettuce"),
            Ingredient(pk=4, name="Tomato",),
            Ingredient(pk=5, name="Garnish",)
        ]
        recipe = Recipe(pk=1, title="BLT", uploaded=datetime.now())
        ingredients_in_recipe = [
            IngredientInRecipe(pk=1, ingredient_key=1, recipe_key=1,
                               optional=False, count=2,
                               unit_of_measure="slice", units_plural="slices"),
            IngredientInRecipe(pk=2, ingredient_key=2, recipe_key=1,
                               optional=False, count=3,
                               unit_of_measure="strip", units_plural="strips"),
            IngredientInRecipe(pk=3, ingredient_key=3, recipe_key=1,
                               optional=False, count=2,
                               unit_of_measure="leaf", units_plural="leaves"),
            IngredientInRecipe(pk=4, ingredient_key=4, recipe_key=1,
                               optional=False, count=1,
                               unit_of_measure="slice", units_plural="slices"),
            IngredientInRecipe(pk=5, ingredient_key=5, recipe_key=1,
                               optional=True, count=None,
                               unit_of_measure=None)
        ]

        db.session.add_all(ingredients)
        db.session.add(recipe)
        db.session.commit()

        db.session.add_all(ingredients_in_recipe)
        db.session.commit()
