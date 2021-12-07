from ..models import (
    ALL_TABLES, DROP_ORDER,
    User, UserProfile,
    Ingredient, Recipe, IngredientInRecipe, InstructionInRecipe,
    Kitchenware, KitchenwareInRecipe, RecipeRating, RecipeComment,
    MediaInRecipe
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
        kitchenware_in_recipe = [
            KitchenwareInRecipe(pk=1, kitchenware_key=1,
                                recipe_key=1, optional=False),
            KitchenwareInRecipe(pk=2, kitchenware_key=1,
                                recipe_key=2, optional=True),
            KitchenwareInRecipe(pk=3, kitchenware_key=1,
                                recipe_key=3, optional=False),
            KitchenwareInRecipe(pk=4, kitchenware_key=1,
                                recipe_key=4, optional=False),
        ]
        recipes = [
            Recipe(pk=1, title="BLT 🥪",
                   subtitle="Bacon lettuce & tomato sandwich",
                   description="MM...FOOD\nYummy BLT!",
                   uploaded=datetime.now(), uploaded_by=1),
            Recipe(pk=2, title="Bread sandwich",
                   subtitle="Traditional British bread sandwich",
                   description="Enjoy this traditional British lunch sandwich!",
                   uploaded=datetime.now(), uploaded_by=2),
            Recipe(pk=3, title="Salad",
                   subtitle="Gross",
                   description="I hate salad",
                   uploaded=datetime.now(), uploaded_by=1),
            Recipe(pk=4, title="Help me",
                   subtitle="I need help immediately",
                   description="This is a cry for help.",
                   uploaded=datetime.now(), uploaded_by=1)
        ]
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
                               optional=True),
            IngredientInRecipe(pk=6, ingredient_key=1, recipe_key=2,
                               optional=False),
            IngredientInRecipe(pk=7, ingredient_key=3, recipe_key=3,
                               optional=False),
            IngredientInRecipe(pk=8, ingredient_key=4, recipe_key=3,
                               optional=False),
            IngredientInRecipe(pk=9, ingredient_key=2, recipe_key=4,
                               optional=False)
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
            InstructionInRecipe(pk=7, recipe_key=2,
                                description="Bread sandwich lol!",
                                instruction_number=1,
                                optional=False),
            InstructionInRecipe(pk=8, recipe_key=2,
                                description="Consume.",
                                instruction_number=2,
                                optional=False),
            InstructionInRecipe(pk=9, recipe_key=3,
                                description="Seriously who eats salad lol",
                                instruction_number=1,
                                optional=False),
            InstructionInRecipe(pk=10, recipe_key=4,
                                description="DROP DATABASE recipebuddy;",
                                instruction_number=1,
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
        media_in_recipe = [
            MediaInRecipe(pk=1, recipe_key=1,
                          media_link="NAh9oLs67Cw",
                          is_video=True),
            MediaInRecipe(pk=2, recipe_key=1,
                          media_link="https://i.imgur.com/KSDywdy.jpeg",
                          is_video=False),
            MediaInRecipe(pk=3, recipe_key=2,
                          media_link="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/An_image_of_a_toast_sandwich%2C_shot_from_the_side.jpg/800px-An_image_of_a_toast_sandwich%2C_shot_from_the_side.jpg",
                          is_video=False),
            MediaInRecipe(pk=4, recipe_key=3,
                          media_link="https://i.imgur.com/2YvUswr.png",
                          is_video=False),
            MediaInRecipe(pk=5, recipe_key=4,
                          media_link="GhTjEk9nr3Q",
                          is_video=True)
        ]

        user_profiles = [
            UserProfile(uid=1, favorite_recipe=1, has_profile_photo=False),
            UserProfile(uid=2, favorite_recipe=1, has_profile_photo=False)
        ]

        db.session.add_all(users)
        db.session.commit()

        db.session.add_all(ingredients)
        db.session.add(kitchenware)
        db.session.add_all(recipes)
        db.session.commit()

        db.session.add_all(instructions)
        db.session.add_all(ingredients_in_recipe)
        db.session.add_all(kitchenware_in_recipe)
        db.session.add_all(media_in_recipe)
        db.session.add(rating)
        db.session.add_all(comments)
        db.session.add_all(user_profiles)
        db.session.commit()
