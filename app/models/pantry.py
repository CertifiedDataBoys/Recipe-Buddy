from sqlalchemy.orm import relationship
from .database import db
from dataclasses import dataclass
from .food import Ingredient
from .user import User


@dataclass
class PantryIngredient(db.Model):
    """
        This model represents an ingredient in a pantry.

        Attributes:
            pk (db.Integer):
                        The primary key of this pantry item.
            uid (db.Integer):
                        The uid of the user whose pantry we are looking at.
            ingredient_key (db.Integer):
                        The primary key of the ingredient in the pantry.
            count (db.Integer):
                        The amount of this ingredient that is in the pantry.
    """

    pk: int
    uid: int
    ingredient_key: int
    count: int

    pk = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey("user.uid"),
                    nullable=False)
    ingredient_key = db.Column(db.Integer, db.ForeignKey("ingredient.pk"),
                               nullable=False)
    count = db.Column(db.Integer, nullable=False)


@dataclass
class PantryKitchenware(db.Model):
    """
        This model represents an ingredient in a pantry.

        Attributes:
            pk (db.Integer):
                        The primary key of this pantry item.
            uid (db.Integer):
                        The uid of the user whose pantry we are looking at.
            kitchenware_key (db.Integer):
                        The primary key of the kitchenware in the pantry.
            in_kitchen (db.Boolean):
                        Is this kitchenware still in the kitchen?
    """

    pk: int
    uid: int
    kitchenware_key: int
    in_kitchen: bool

    pk = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey("user.uid"),
                    nullable=False)
    kitchenware_key = db.Column(db.Integer, db.ForeignKey("kitchenware.pk"),
                                nullable=False)
    in_kitchen = db.Column(db.Boolean, nullable=False)
