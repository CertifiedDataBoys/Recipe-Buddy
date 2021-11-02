from .database import db


class Ingredient(db.Model):
    """
        This model represents an ingredient.

        Attributes:
            pk (db.Integer):
                        Primary key
            name (db.String(64)):
                        The name of the ingredient
            unit_of_measure (db.String(32)):
                        The unit of measure for this ingredient
            units_plural (db.String(32)):
                        The plural version of our unit of measure
    """

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    unit_of_measure = db.Column(db.String(32), unique=False, nullable=True)
    units_plural = db.Column(db.String(32), unique=False, nullable=True)


class Kitchenware(db.Model):
    """
        This model represents kitchenware.

        Attributes:
            pk (db.Integer):
                        Primary key
            name (db.String(64)):
                        The name of the kitchenware
    """

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)


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
            uploaded_by (db.Integer):
                        The primary key of the user who uploaded this recipe
    """

    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=False, nullable=False)
    uploaded = db.Column(db.DateTime(), unique=False, nullable=False)
    uploaded_by = db.Column(db.Integer, db.ForeignKey("user.uid"),
                            nullable=False)


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


class KitchenwareInRecipe(db.Model):
    """
        This model represents the ingredients that go into a recipe. It links
        kitchenware to recipes using their primary keys.

        Attributes:
            pk (db.Integer):
                        Primary key
            kitchenware_key (db.Integer):
                        The primary key of some given kitchenware
            recipe_key (db.Integer):
                        The primary key of a given recipe
            optional (db.Boolean):
                        Boolean representing if this ingredient is optional or
                        not
    """
    pk = db.Column(db.Integer, primary_key=True)
    kitchenware_key = db.Column(db.Integer, db.ForeignKey("kitchenware.pk"),
                                nullable=False)
    recipe_key = db.Column(db.Integer, db.ForeignKey("recipe.pk"),
                           nullable=False)
    optional = db.Column(db.Boolean, nullable=False)
