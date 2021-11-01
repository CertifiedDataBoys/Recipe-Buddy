from .database import db
from sqlalchemy.ext.declarative import declared_attr


class InteractionMixin(object):

    __tablename__ = "interaction"

    pk = db.Column(db.Integer, primary_key=True)
    @declared_attr
    def uid(self):
        return db.Column(db.Integer, db.ForeignKey("user.uid"), nullable=False)
    times_accessed = db.Column(db.Integer, unique=False, nullable=False)
    first_accessed = db.Column(db.DateTime(), unique=False, nullable=False)
    last_accessed = db.Column(db.DateTime(), unique=False, nullable=False)


class RecipeRating(db.Model):

    pk = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey("user.uid"), nullable=False)
    recipe_key = db.Column(db.Integer, db.ForeignKey("recipe.pk"),
                           nullable=False)
    rating = db.Column(db.Float, nullable=False)


class UserInteractionIngredient(InteractionMixin, db.Model):

    __tablename__ = "user_interaction_ingredient"

    ingredient_key = db.Column(db.Integer, db.ForeignKey("ingredient.pk"),
                               nullable=False)


class UserInteractionKitchenware(InteractionMixin, db.Model):

    __tablename__ = "user_interaction_kitchenware"

    kitchenware_key = db.Column(db.Integer, db.ForeignKey("kitchenware.pk"),
                                nullable=False)


class UserInteractionRecipe(InteractionMixin, db.Model):

    __tablename__ = "user_interaction_recipe"

    recipe_key = db.Column(db.Integer, db.ForeignKey("recipe.pk"),
                           nullable=False)


class UserInteractionSearch(InteractionMixin, db.Model):

    __tablename__ = "user_interaction_search"

    search_term = db.Column(db.String(256), unique=False, nullable=False)


class UserInteractionProfile(InteractionMixin, db.Model):

    __tablename__ = "user_interaction_profile"

    profile_accessed = db.Column(db.Integer, db.ForeignKey("user.uid"))
