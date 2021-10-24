from ..models import User, Ingredient, Recipe, IngredientInRecipe
from datetime import datetime
import hashlib


def drop_db_tables(app, db):
    """
        Drop our database tables that we are testing.
        This means that we need to drop the User, Recipe, Ingredient, and
            IngredientInRecipe tables.

        Args:
            app (Flask):
                        The Flask app representing Recipe Buddy
            db (SQLAlchemy):
                        The SQLAlchemy object we use to connect to our database
    """

    with app.app_context():

        IngredientInRecipe.__table__.drop(db.engine)
        Ingredient.__table__.drop(db.engine)
        Recipe.__table__.drop(db.engine)
        User.__table__.drop(db.engine)
        db.session.commit()


def delete_db_entries(app, db):
    """
        Drop our database testing data, but keep the tables intact.

        Args:
            app (Flask):
                        The Flask app representing Recipe Buddy
            db (SQLAlchemy):
                        The SQLAlchemy object we use to connect to our database
    """

    with app.app_context():

        IngredientInRecipe.query.delete()
        db.session.commit()

        Ingredient.query.delete()
        Recipe.query.delete()
        db.session.commit()

        User.query.delete()
        db.session.commit()


def create_db_tables(app, db):
    """
        Create the database tables that we are testing.
        This means that we need to create the User, Recipe, Ingredient, and
            IngredientInRecipe tables.

        Args:
            app (Flask):
                        The Flask app representing Recipe Buddy
            db (SQLAlchemy):
                        The SQLAlchemy object we use to connect to our database
    """

    with app.app_context():

        db.create_all()
        db.session.commit()


def create_db_test_data(app, db):
    """
        Populate the database tables that we are testing with some dummy data.
        This means that we need to populate the User, Recipe, Ingredient, and
            IngredientInRecipe tables.

        Args:
            app (Flask):
                        The Flask app representing Recipe Buddy
            db (SQLAlchemy):
                        The SQLAlchemy object we use to connect to our database
    """

    with app.app_context():

        user = User(uid=1, username="big_sean_banerjee",
                    email="sean@k.banerjee.net",
                    verified=True)
        user.set_password("YouShouldHaveStartedCodingByNow")
        ingredients = [
            Ingredient(pk=1, name="Bread",
                       unit_of_measure="slice", units_plural="slices"),
            Ingredient(pk=2, name="Bacon",
                       unit_of_measure="strip", units_plural="strips"),
            Ingredient(pk=3, name="Lettuce",
                       unit_of_measure="leaf", units_plural="leaves"),
            Ingredient(pk=4, name="Tomato",
                       unit_of_measure="slice", units_plural="slices"),
            Ingredient(pk=5, name="Garnish")
        ]
        recipe = Recipe(pk=1, title="BLT",
                        uploaded=datetime.now(), uploaded_by=1)
        ingredients_in_recipe = [
            IngredientInRecipe(pk=1, ingredient_key=1, recipe_key=1,
                               optional=False, count=2),
            IngredientInRecipe(pk=2, ingredient_key=2, recipe_key=1,
                               optional=False, count=3),
            IngredientInRecipe(pk=3, ingredient_key=3, recipe_key=1,
                               optional=False, count=2),
            IngredientInRecipe(pk=4, ingredient_key=4, recipe_key=1,
                               optional=False, count=1),
            IngredientInRecipe(pk=5, ingredient_key=5, recipe_key=1,
                               optional=True)
        ]

        db.session.add(user)
        db.session.commit()

        db.session.add_all(ingredients)
        db.session.add(recipe)
        db.session.commit()

        db.session.add_all(ingredients_in_recipe)
        db.session.commit()
