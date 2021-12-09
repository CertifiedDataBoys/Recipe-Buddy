from .database import db
from dataclasses import dataclass
from datetime import timedelta


@dataclass
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

    pk: int
    name: str
    unit_of_measure: str
    units_plural: str

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False, nullable=False)
    unit_of_measure = db.Column(db.String(32), unique=False, nullable=True)
    units_plural = db.Column(db.String(32), unique=False, nullable=True)


@dataclass
class Kitchenware(db.Model):
    """
        This model represents kitchenware.

        Attributes:
            pk (db.Integer):
                        Primary key
            name (db.String(64)):
                        The name of the kitchenware
    """

    pk: int
    name: str

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)


@dataclass
class Recipe(db.Model):
    """
        This model represents a recipe.

        Attributes:
            pk (db.Integer):
                        Primary key
            title (db.String(64)):
                        The title of the recipe
            subtitle (db.String(64)):
                        The subtitle of the recipe (optional)
            description (db.String(4096)):
                        The description of the recipe. Instructions are
                            separate.
            uploaded (db.DateTime):
                        A DateTime object showing when this recipe was uploaded
            uploaded_by (db.Integer):
                        The primary key of the user who uploaded this recipe
    """

    pk: int
    title: str
    subtitle: str
    description: str
    uploaded: timedelta
    uploaded_by: int

    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=False, nullable=False)
    subtitle = db.Column(db.String(64), unique=False, nullable=True)
    description = db.Column(db.String(4096), unique=False, nullable=False)
    uploaded = db.Column(db.DateTime(), unique=False, nullable=False)
    uploaded_by = db.Column(db.Integer, db.ForeignKey("user.uid"),
                            nullable=False)


@dataclass
class InstructionInRecipe(db.Model):
    """
        This model represents an instruction in a recipe.

        Attributes:
            pk (db.Integer):
                        Primary key
            recipe_key (db.Integer):
                        The primary key of a given recipe
            description (db.String(2048)):
                        The description of this instruction
            instruction_number (db.Integer):
                        Number signifying which step this is in our process
            optional (db.Boolean):
                        Is this instruction optional or not?
    """

    pk: int
    recipe_key: int
    description: str
    instruction_number: int
    optional: bool

    pk = db.Column(db.Integer, primary_key=True)
    recipe_key = db.Column(db.Integer, db.ForeignKey("recipe.pk"),
                           nullable=False)
    description = db.Column(db.String(2048), unique=False, nullable=False)
    instruction_number = db.Column(db.Integer, unique=False, nullable=False)
    optional = db.Column(db.Boolean, unique=False, nullable=False)


@dataclass
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

    pk: int
    ingredient_key: int
    recipe_key: int
    optional: bool
    count: int

    pk = db.Column(db.Integer, primary_key=True)
    ingredient_key = db.Column(db.Integer, db.ForeignKey("ingredient.pk"),
                               nullable=False)
    recipe_key = db.Column(db.Integer, db.ForeignKey("recipe.pk"),
                           nullable=False)
    optional = db.Column(db.Boolean, nullable=False)
    count = db.Column(db.Integer, nullable=True)


@dataclass
class KitchenwareInRecipe(db.Model):
    """
        This model represents the kitchenware that go into a recipe. It links
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

    pk: int
    kitchenware_key: int
    recipe_key: int
    optional: bool

    pk = db.Column(db.Integer, primary_key=True)
    kitchenware_key = db.Column(db.Integer, db.ForeignKey("kitchenware.pk"),
                                nullable=False)
    recipe_key = db.Column(db.Integer, db.ForeignKey("recipe.pk"),
                           nullable=False)
    optional = db.Column(db.Boolean, nullable=False)


@dataclass
class MediaInRecipe(db.Model):
    """
        This model represents the media on a recipe's page. It links
        media to recipes using the media_link string.

        Attributes:
            pk (db.Integer):
                        Primary key
            recipe_key (db.Integer):
                        The primary key of a given recipe
            media_link (db.String):
                        A link to some given media. Can be a direct link to an
                        image or a youtube embed code. Can be up to 512
                        characters long
            is_video (db.Boolean):
                        Boolean representing if this media is a youtube video or
                        not
    """

    pk: int
    recipe_key: int
    media_link: str
    is_video: bool

    pk = db.Column(db.Integer, primary_key=True)
    recipe_key = db.Column(db.Integer, db.ForeignKey("recipe.pk"),
                           nullable=False)
    media_link = db.Column(db.String(512), nullable=False)
    is_video = db.Column(db.Boolean, nullable=False)
