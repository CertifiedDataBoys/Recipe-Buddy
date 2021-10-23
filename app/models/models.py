from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Ingredient(db.Model):
    """
        This model represents an ingredient.

        Attributes:
            pk (db.Integer):
                        Primary key
            name (db.String(64)):
                        The name of the ingredient
            unit_of_measure (db.String(32)):
                        What is our unit of measure for this ingredient?
            units_plural (db.String(32)):
                        What is the plural version of our unit of measure?
    """

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    unit_of_measure = db.Column(db.String(32), unique=False, nullable=True)
    units_plural = db.Column(db.String(32), unique=False, nullable=True)


class Recipe(db.Model):
    """
        This model represents a recipe.

        Attributes:
            pk (db.Integer):
                        Primary key
            title (db.String(64)):
                        The title of the recipe
            uploaded (db.DateTime):
                        A DateTime object showing when this recipe was uploaded
    """

    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=False, nullable=False)
    uploaded = db.Column(db.DateTime(), unique=False, nullable=False)


class IngredientInRecipe(db.Model):
    """
        This model represents the ingredients that go into a recipe. It links
        ingredients to recipes using their primary keys.

        Attributes:
            pk (db.Integer):
                        Primary key
            ingredient_key (db.Integer):
                        The primary key of a given ingredient
            recipe_key (db.Integer):
                        The primary key of a given recipe
            optional (db.Boolean):
                        Boolean representing if this ingredient is optional or
                        not
            count (db.Integer):
                        Represents how much of the ingredient we should use.
                        Can be left blank.
    """

    pk = db.Column(db.Integer, primary_key=True)
    ingredient_key = db.Column(db.Integer, db.ForeignKey("ingredient.pk"),
                               nullable=False)
    recipe_key = db.Column(db.Integer, db.ForeignKey("recipe.pk"),
                               nullable=False)
    optional = db.Column(db.Boolean, nullable=False)
    count = db.Column(db.Integer, nullable=True)
