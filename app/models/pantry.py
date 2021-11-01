from sqlalchemy.orm import relationship
from .database import db
from .food import Ingredient
from .user import User


class PantryIngredient(db.Model):

    pk = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey("user.uid"),
                    nullable=False)
    ingredient_key = db.Column(db.Integer, db.ForeignKey("ingredient.pk"),
                               nullable=False)
    count = db.Column(db.Integer, nullable=False)


class PantryKitchenware(db.Model):

    pk = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey("user.uid"),
                    nullable=False)
    kitchenware_key = db.Column(db.Integer, db.ForeignKey("kitchenware.pk"),
                                nullable=False)
    in_kitchen = db.Column(db.Boolean, nullable=False)
