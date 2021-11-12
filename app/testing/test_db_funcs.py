from ..models import (
    ALL_TABLES, DROP_ORDER,
    User, Ingredient, Recipe, IngredientInRecipe, InstructionInRecipe,
    Kitchenware, KitchenwareInRecipe, RecipeRating, RecipeComment
)
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

        for table in DROP_ORDER:
            print(table.__table__)
            table.__table__.drop(db.engine)
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

        for table in DROP_ORDER:
            table.query.delete()
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

        users = [
            User(uid=1, username="big_sean_banerjee",
                 email="sean@k.banerjee.net",
                 verified=True),
            User(uid=2, username="KingoFan",
                 email="kingo@fan.club",
                 verified=True)
        ]
        users[0].set_password("CS350-Project")
        users[1].set_password("IL0veKingo!")
        ingredients = [
            Ingredient(pk=1, name="Bread 🍞",
                       unit_of_measure="slice", units_plural="slices"),
            Ingredient(pk=2, name="Bacon 🥓",
                       unit_of_measure="strip", units_plural="strips"),
            Ingredient(pk=3, name="Lettuce 🥬",
                       unit_of_measure="leaf", units_plural="leaves"),
            Ingredient(pk=4, name="Tomato 🍅",
                       unit_of_measure="slice", units_plural="slices"),
            Ingredient(pk=5, name="Garnish 🌸")
        ]
        kitchenware = Kitchenware(pk=1, name="Knife")
        kitchenware_in_recipe = KitchenwareInRecipe(
            pk=1, kitchenware_key=1, recipe_key=1, optional=False
        )
        recipe = Recipe(pk=1, title="BLT 🥪",
                        subtitle="Bacon lettuce & tomato sandwich",
                        description="MM...FOOD\nYummy BLT!",
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
        instructions = [
            InstructionInRecipe(pk=1, recipe_key=1,
                                description="Place a slab of bread on a plate.",
                                instruction_number=1,
                                optional=False),
            InstructionInRecipe(pk=2, recipe_key=1,
                                description="Fry up your (yummy) bacon until" +
                                            " crispy.",
                                instruction_number=2,
                                optional=False),
            InstructionInRecipe(pk=3, recipe_key=1,
                                description="Place bacon, whole lettuce, and" +
                                             " whole tomatos on your bread in" +
                                             " that specific order.",
                                instruction_number=3,
                                optional=False),
            InstructionInRecipe(pk=4, recipe_key=1,
                                description="Place a slab of bread on top of" +
                                            " your newly-assembled BLT.",
                                instruction_number=4,
                                optional=False),
            InstructionInRecipe(pk=5, recipe_key=1,
                                description="Garnish your sandwich as desired.",
                                instruction_number=5,
                                optional=True),
            InstructionInRecipe(pk=6, recipe_key=1,
                                description="Enjoy!",
                                instruction_number=6,
                                optional=False),
        ]
        rating = RecipeRating(pk=1, uid=1, recipe_key=1, rating=4.5)
        comments = [
            RecipeComment(pk=1, recipe_key=1, uid=2, reply_to=None,
                          contents="in theaters November 5th",
                          uploaded=datetime.now(),
                          suggestion=True),
            RecipeComment(pk=2, recipe_key=1, uid=2, reply_to=None,
                          contents="kingokingokingokingokingo",
                          uploaded=datetime.now(),
                          suggestion=False),
            RecipeComment(pk=3, recipe_key=1, uid=1, reply_to=1,
                          contents="out now",
                          uploaded=datetime.now(),
                          suggestion=False),
            RecipeComment(pk=4, recipe_key=1, uid=1, reply_to=3,
                          contents="no way",
                          uploaded=datetime.now(),
                          suggestion=False),
            RecipeComment(pk=5, recipe_key=1, uid=2, reply_to=1,
                          contents="kingo meal @ mcdonalds",
                          uploaded=datetime.now(),
                          suggestion=False)
        ]

        db.session.add_all(users)
        db.session.commit()

        db.session.add_all(ingredients)
        db.session.add(kitchenware)
        db.session.add(recipe)
        db.session.commit()

        db.session.add_all(instructions)
        db.session.add_all(ingredients_in_recipe)
        db.session.add(kitchenware_in_recipe)
        db.session.add(rating)
        db.session.add_all(comments)
        db.session.commit()
