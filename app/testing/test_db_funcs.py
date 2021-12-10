from ..models import (
    ALL_TABLES, DROP_ORDER,
    User, UserProfile,
    Ingredient, Recipe, IngredientInRecipe, InstructionInRecipe,
    Kitchenware, KitchenwareInRecipe, RecipeRating, RecipeComment,
    MediaInRecipe, DietaryRestriction, RestrictionOnIngredient,
    UserDietaryRestriction
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
            User(uid=1, username="ProfessorBanerjee",
                 email="sean@k.banerjee.net",
                 verified=True,
                 is_manager=True),
            User(uid=2, username="RecipeBuddyUser",
                 email="user@recipebuddy.com",
                 verified=True,
                 is_manager=True),
        ]
        users[0].set_password("CS350-Project")
        users[1].set_password("RecipeBuddyPassword1!")
        ingredients = [
            Ingredient(pk=1, name="Bread 🍞",
                       unit_of_measure="slice", units_plural="slices"),
            Ingredient(pk=2, name="Bacon 🥓",
                       unit_of_measure="strip", units_plural="strips"),
            Ingredient(pk=3, name="Lettuce 🥬",
                       unit_of_measure="leaf", units_plural="leaves"),
            Ingredient(pk=4, name="Tomato 🍅",
                       unit_of_measure="slice", units_plural="slices"),
            Ingredient(pk=5, name="Garnish 🌸"),
            Ingredient(pk=6, name="Loose leaf green tea 🍵",
                       unit_of_measure="teaspoon", units_plural="teaspoons"),
            Ingredient(pk=7, name="Genmai rice 🍚",
                       unit_of_measure="grain", units_plural="grains"),
            Ingredient(pk=8, name="Popcorn 🍿",
                       unit_of_measure="bag", units_plural="bags"),
            Ingredient(pk=9, name="Butter 🧈",
                       unit_of_measure="stick", units_plural="sticks"),
            Ingredient(pk=10, name="Salt 🧂",
                       unit_of_measure="Tablespoon", units_plural="Tablespoons"),
            Ingredient(pk=11, name="Ice 🧊",
                       unit_of_measure="cube", units_plural="cubes"),
            Ingredient(pk=12, name="Cheese 🧀",
                       unit_of_measure="slice", units_plural="slices"),
        ]
        kitchenware = [
            Kitchenware(pk=1, name="Knife"),
            Kitchenware(pk=2, name="Wok"),
            Kitchenware(pk=3, name="Immersion Blender"),
            Kitchenware(pk=4, name="Air Fryer"),
            Kitchenware(pk=5, name="Electric kettle")
        ]
        kitchenware_in_recipe = [
            KitchenwareInRecipe(pk=1, kitchenware_key=1,
                                recipe_key=1, optional=False),
            KitchenwareInRecipe(pk=2, kitchenware_key=4,
                                recipe_key=1, optional=True),
            KitchenwareInRecipe(pk=3, kitchenware_key=1,
                                recipe_key=2, optional=True),
            KitchenwareInRecipe(pk=4, kitchenware_key=1,
                                recipe_key=3, optional=False),
            KitchenwareInRecipe(pk=5, kitchenware_key=1,
                                recipe_key=4, optional=False),
            KitchenwareInRecipe(pk=6, kitchenware_key=5,
                                recipe_key=5, optional=False)
        ]
        restrictions = [
            DietaryRestriction(pk=1, name="Vegan"),
            DietaryRestriction(pk=2, name="Vegetarian"),
            DietaryRestriction(pk=3, name="Dairy-free"),
            DietaryRestriction(pk=4, name="Pescatarian"),
            DietaryRestriction(pk=5, name="Gluten-free"),
            DietaryRestriction(pk=6, name="Keto"),
            DietaryRestriction(pk=7, name="Kosher"),
            DietaryRestriction(pk=8, name="Lactose-free"),
            DietaryRestriction(pk=9, name="Nut-free"),
            DietaryRestriction(pk=10, name="Low carb")
        ]
        user_dietary_restrictions = [
            UserDietaryRestriction(pk=1, uid=1, restriction_key=3),
            UserDietaryRestriction(pk=2, uid=1, restriction_key=7),
            UserDietaryRestriction(pk=3, uid=2, restriction_key=1),
            UserDietaryRestriction(pk=4, uid=2, restriction_key=2),
            UserDietaryRestriction(pk=5, uid=2, restriction_key=3),
            UserDietaryRestriction(pk=6, uid=2, restriction_key=5),
            UserDietaryRestriction(pk=7, uid=2, restriction_key=10),
        ]
        ingredient_restrictions = [
            RestrictionOnIngredient(pk=1, ingredient_key=1, restriction_key=1),
            RestrictionOnIngredient(pk=2, ingredient_key=1, restriction_key=2),
            RestrictionOnIngredient(pk=3, ingredient_key=1, restriction_key=3),
            RestrictionOnIngredient(pk=4, ingredient_key=1, restriction_key=4),
            RestrictionOnIngredient(pk=5, ingredient_key=1, restriction_key=7),
            RestrictionOnIngredient(pk=6, ingredient_key=1, restriction_key=8),
            RestrictionOnIngredient(pk=7, ingredient_key=1, restriction_key=9),
            RestrictionOnIngredient(pk=8, ingredient_key=2, restriction_key=3),
            RestrictionOnIngredient(pk=9, ingredient_key=2, restriction_key=5),
            RestrictionOnIngredient(pk=10, ingredient_key=2, restriction_key=6),
            RestrictionOnIngredient(pk=11, ingredient_key=2, restriction_key=8),
            RestrictionOnIngredient(pk=12, ingredient_key=2, restriction_key=9),
            RestrictionOnIngredient(pk=13, ingredient_key=2, restriction_key=10),
            RestrictionOnIngredient(pk=14, ingredient_key=3, restriction_key=1),
            RestrictionOnIngredient(pk=15, ingredient_key=3, restriction_key=2),
            RestrictionOnIngredient(pk=16, ingredient_key=3, restriction_key=3),
            RestrictionOnIngredient(pk=17, ingredient_key=3, restriction_key=4),
            RestrictionOnIngredient(pk=18, ingredient_key=3, restriction_key=5),
            RestrictionOnIngredient(pk=19, ingredient_key=3, restriction_key=6),
            RestrictionOnIngredient(pk=20, ingredient_key=3, restriction_key=7),
            RestrictionOnIngredient(pk=21, ingredient_key=3, restriction_key=8),
            RestrictionOnIngredient(pk=22, ingredient_key=3, restriction_key=9),
            RestrictionOnIngredient(pk=23, ingredient_key=3, restriction_key=10),
            RestrictionOnIngredient(pk=24, ingredient_key=4, restriction_key=1),
            RestrictionOnIngredient(pk=25, ingredient_key=4, restriction_key=2),
            RestrictionOnIngredient(pk=26, ingredient_key=4, restriction_key=3),
            RestrictionOnIngredient(pk=27, ingredient_key=4, restriction_key=4),
            RestrictionOnIngredient(pk=28, ingredient_key=4, restriction_key=5),
            RestrictionOnIngredient(pk=29, ingredient_key=4, restriction_key=6),
            RestrictionOnIngredient(pk=30, ingredient_key=4, restriction_key=7),
            RestrictionOnIngredient(pk=31, ingredient_key=4, restriction_key=8),
            RestrictionOnIngredient(pk=32, ingredient_key=4, restriction_key=9),
            RestrictionOnIngredient(pk=33, ingredient_key=4, restriction_key=10),
            RestrictionOnIngredient(pk=34, ingredient_key=5, restriction_key=1),
            RestrictionOnIngredient(pk=35, ingredient_key=5, restriction_key=2),
            RestrictionOnIngredient(pk=36, ingredient_key=5, restriction_key=3),
            RestrictionOnIngredient(pk=37, ingredient_key=5, restriction_key=4),
            RestrictionOnIngredient(pk=38, ingredient_key=5, restriction_key=5),
            RestrictionOnIngredient(pk=39, ingredient_key=5, restriction_key=6),
            RestrictionOnIngredient(pk=40, ingredient_key=5, restriction_key=7),
            RestrictionOnIngredient(pk=41, ingredient_key=5, restriction_key=8),
            RestrictionOnIngredient(pk=42, ingredient_key=5, restriction_key=9),
            RestrictionOnIngredient(pk=43, ingredient_key=5, restriction_key=10),
            RestrictionOnIngredient(pk=44, ingredient_key=6, restriction_key=1),
            RestrictionOnIngredient(pk=45, ingredient_key=6, restriction_key=2),
            RestrictionOnIngredient(pk=46, ingredient_key=6, restriction_key=3),
            RestrictionOnIngredient(pk=47, ingredient_key=6, restriction_key=4),
            RestrictionOnIngredient(pk=48, ingredient_key=6, restriction_key=5),
            RestrictionOnIngredient(pk=49, ingredient_key=6, restriction_key=6),
            RestrictionOnIngredient(pk=50, ingredient_key=6, restriction_key=7),
            RestrictionOnIngredient(pk=51, ingredient_key=6, restriction_key=8),
            RestrictionOnIngredient(pk=52, ingredient_key=6, restriction_key=9),
            RestrictionOnIngredient(pk=53, ingredient_key=6, restriction_key=10),
            RestrictionOnIngredient(pk=54, ingredient_key=7, restriction_key=1),
            RestrictionOnIngredient(pk=55, ingredient_key=7, restriction_key=2),
            RestrictionOnIngredient(pk=56, ingredient_key=7, restriction_key=3),
            RestrictionOnIngredient(pk=57, ingredient_key=7, restriction_key=4),
            RestrictionOnIngredient(pk=58, ingredient_key=7, restriction_key=5),
            RestrictionOnIngredient(pk=59, ingredient_key=7, restriction_key=6),
            RestrictionOnIngredient(pk=60, ingredient_key=7, restriction_key=7),
            RestrictionOnIngredient(pk=61, ingredient_key=7, restriction_key=8),
            RestrictionOnIngredient(pk=62, ingredient_key=7, restriction_key=9),
            RestrictionOnIngredient(pk=63, ingredient_key=7, restriction_key=10),
            RestrictionOnIngredient(pk=64, ingredient_key=8, restriction_key=1),
            RestrictionOnIngredient(pk=65, ingredient_key=8, restriction_key=2),
            RestrictionOnIngredient(pk=66, ingredient_key=8, restriction_key=3),
            RestrictionOnIngredient(pk=67, ingredient_key=8, restriction_key=4),
            RestrictionOnIngredient(pk=68, ingredient_key=8, restriction_key=5),
            RestrictionOnIngredient(pk=69, ingredient_key=8, restriction_key=6),
            RestrictionOnIngredient(pk=70, ingredient_key=8, restriction_key=7),
            RestrictionOnIngredient(pk=71, ingredient_key=8, restriction_key=8),
            RestrictionOnIngredient(pk=72, ingredient_key=8, restriction_key=9),
            RestrictionOnIngredient(pk=73, ingredient_key=8, restriction_key=10),
            RestrictionOnIngredient(pk=74, ingredient_key=8, restriction_key=1),
            RestrictionOnIngredient(pk=75, ingredient_key=8, restriction_key=2),
            RestrictionOnIngredient(pk=76, ingredient_key=9, restriction_key=4),
            RestrictionOnIngredient(pk=77, ingredient_key=9, restriction_key=5),
            RestrictionOnIngredient(pk=78, ingredient_key=9, restriction_key=6),
            RestrictionOnIngredient(pk=79, ingredient_key=9, restriction_key=7),
            RestrictionOnIngredient(pk=80, ingredient_key=9, restriction_key=9),
            RestrictionOnIngredient(pk=81, ingredient_key=9, restriction_key=10),
            RestrictionOnIngredient(pk=82, ingredient_key=10, restriction_key=1),
            RestrictionOnIngredient(pk=83, ingredient_key=10, restriction_key=2),
            RestrictionOnIngredient(pk=84, ingredient_key=10, restriction_key=3),
            RestrictionOnIngredient(pk=85, ingredient_key=10, restriction_key=4),
            RestrictionOnIngredient(pk=86, ingredient_key=10, restriction_key=5),
            RestrictionOnIngredient(pk=87, ingredient_key=10, restriction_key=6),
            RestrictionOnIngredient(pk=88, ingredient_key=10, restriction_key=7),
            RestrictionOnIngredient(pk=89, ingredient_key=10, restriction_key=8),
            RestrictionOnIngredient(pk=90, ingredient_key=10, restriction_key=9),
            RestrictionOnIngredient(pk=91, ingredient_key=10, restriction_key=10),
            RestrictionOnIngredient(pk=92, ingredient_key=11, restriction_key=1),
            RestrictionOnIngredient(pk=93, ingredient_key=11, restriction_key=2),
            RestrictionOnIngredient(pk=94, ingredient_key=11, restriction_key=4),
            RestrictionOnIngredient(pk=95, ingredient_key=11, restriction_key=5),
            RestrictionOnIngredient(pk=96, ingredient_key=11, restriction_key=6),
            RestrictionOnIngredient(pk=97, ingredient_key=11, restriction_key=7),
            RestrictionOnIngredient(pk=98, ingredient_key=11, restriction_key=9),
            RestrictionOnIngredient(pk=99, ingredient_key=11, restriction_key=10)
        ]
        recipes = [
            Recipe(pk=1, title="BLT 🥪",
                   subtitle="Bacon lettuce & tomato sandwich",
                   description="MM...FOOD\nYummy BLT!",
                   type="Sandwich",
                   uploaded=datetime.now(), uploaded_by=1),
            Recipe(pk=2, title="Bread sandwich",
                   subtitle="Traditional British bread sandwich",
                   description="Enjoy this traditional British lunch sandwich!",
                   type="Sandwich",
                   uploaded=datetime.now(), uploaded_by=2),
            Recipe(pk=3, title="Side salad",
                   subtitle="Gross",
                   description="I hate salad",
                   type="Side",
                   uploaded=datetime.now(), uploaded_by=1),
            Recipe(pk=4, title="Sodexo Platter",
                   subtitle="This is a platter",
                   description="Image definately not taken at Clarkson.",
                   type="Vegan",
                   uploaded=datetime.now(), uploaded_by=1),
            Recipe(pk=5, title="Popcorn Tea",
                   subtitle="Also known as Genmaicha Tea",
                   description="A popular type of Japanese Tea, Popcorn Tea is genmaicha tea (green tea with popped brown rice) brewed with popcorn!",
                   type="Drink",
                   uploaded=datetime.now(), uploaded_by=2)
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
                               optional=True, count=1),
            IngredientInRecipe(pk=6, ingredient_key=12, recipe_key=1,
                               optional=True, count=1),
            IngredientInRecipe(pk=7, ingredient_key=1, recipe_key=2,
                               optional=False, count=3),
            IngredientInRecipe(pk=8, ingredient_key=3, recipe_key=3,
                               optional=False, count=5),
            IngredientInRecipe(pk=9, ingredient_key=4, recipe_key=3,
                               optional=False, count=1),
            IngredientInRecipe(pk=10, ingredient_key=3, recipe_key=4,
                               optional=False, count=1),
            IngredientInRecipe(pk=11, ingredient_key=6, recipe_key=5,
                               optional=False, count=1),
            IngredientInRecipe(pk=12, ingredient_key=7, recipe_key=5,
                               optional=False, count=150),
            IngredientInRecipe(pk=13, ingredient_key=8, recipe_key=5,
                               optional=False, count=1),
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
                                " that specific order. Optionally, add cheese" +
                                " between your bacon and your lettuce.",
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
                                description="Ready to go, consume",
                                instruction_number=1,
                                optional=False),
            InstructionInRecipe(pk=11, recipe_key=5,
                                description="Toast your genmai rice until dark",
                                instruction_number=1,
                                optional=False),
            InstructionInRecipe(pk=12, recipe_key=5,
                                description="Mix your rice with your green tea leaves",
                                instruction_number=2,
                                optional=False),
            InstructionInRecipe(pk=13, recipe_key=5,
                                description="Throw your tea and rice mixture into boiling water for 3 to 5 minutes, depending on preference.",
                                instruction_number=3,
                                optional=False),
            InstructionInRecipe(pk=14, recipe_key=5,
                                description="Add ice to cool down your tea faster",
                                instruction_number=4,
                                optional=True),
            InstructionInRecipe(pk=15, recipe_key=5,
                                description="Enjoy! :D",
                                instruction_number=5,
                                optional=False)
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
                          media_link="uOXlG8Tglc8",
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
                          media_link="yJ32K5vKVfE",
                          is_video=True),
            MediaInRecipe(pk=6, recipe_key=4,
                          media_link="https://content-service.sodexomyway.com/media/healthy-food-background-autumn-fresh-vegetables-dark-stone-table-with-copy-space-top-view_127032-1954_tcm984-128711.jpg?url=https://clarksondining.com/",
                          is_video=False),
            MediaInRecipe(pk=7, recipe_key=5,
                          media_link="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F789031.jpg",
                          is_video=False)
        ]

        user_profiles = [
            UserProfile(uid=1, favorite_recipe=1, has_profile_photo=False),
            UserProfile(uid=2, favorite_recipe=1, has_profile_photo=False)
        ]

        db.session.add_all(users)
        db.session.commit()

        db.session.add_all(ingredients)
        db.session.add_all(kitchenware)
        db.session.add_all(recipes)
        db.session.add_all(restrictions)
        db.session.commit()

        db.session.add_all(user_dietary_restrictions)
        db.session.add_all(ingredient_restrictions)
        db.session.add_all(instructions)
        db.session.add_all(ingredients_in_recipe)
        db.session.add_all(kitchenware_in_recipe)
        db.session.add_all(media_in_recipe)
        db.session.add(rating)
        db.session.add_all(comments)
        db.session.add_all(user_profiles)
        db.session.commit()
