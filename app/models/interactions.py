from .database import db
from dataclasses import dataclass
from datetime import timedelta
from sqlalchemy.ext.declarative import declared_attr


class InteractionMixin(object):
    """
        This class represents common data shared between user interaction
            models.

        Attributes:
            __tablename__ (str):
                        The default name of a user interaction database table.
                            Set to <tt>interaction</tt> by default.
            pk (db.Integer):
                        The primary key of a given user interaction model.
            times_accessed (db.Integer):
                        How many times has a user interacted with this data?
            first_accessed (db.DateTime):
                        When did the user first interact with this data?
            password_hash (db.DateTime):
                        When did the user last interact with this data?
    """

    __tablename__: str
    pk: int
    times_accessed: int
    first_accessed: timedelta
    last_accessed: timedelta

    __tablename__ = "interaction"

    pk = db.Column(db.Integer, primary_key=True)

    @declared_attr
    def uid(self):
        """
            Function to return a user's uid. Call this function like it is
                an attribute (i.e. <tt>UserInteractionModel.uid</tt>.)
        """
        return db.Column(db.Integer, db.ForeignKey("user.uid"), nullable=False)
    times_accessed = db.Column(db.Integer, unique=False, nullable=False)
    first_accessed = db.Column(db.DateTime(), unique=False, nullable=False)
    last_accessed = db.Column(db.DateTime(), unique=False, nullable=False)


@dataclass
class RecipeRating(db.Model):
    """
        This model represents recipe ratings.

        Attributes:
            pk (db.Integer):
                        The primary key of a given recipe rating.
            uid (db.Integer):
                        The uid of the user who left this rating.
            recipe_key (db.Integer):
                        The primary key of the recipe being rated.
            rating (db.Float):
                        What rating did the user give to this recipe?
    """

    pk: int
    uid: int
    recipe_key: int
    rating: float

    pk = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey("user.uid"), nullable=False)
    recipe_key = db.Column(db.Integer, db.ForeignKey("recipe.pk"),
                           nullable=False)
    rating = db.Column(db.Float, nullable=False)


@dataclass
class RecipeComment(db.Model):
    """
        This model represents recipe comments.

        Attributes:
            pk (db.Integer):
                        The primary key of a given recipe comment.
            uid (db.Integer):
                        The uid of the user who left this comment.
            recipe_key (db.Integer):
                        The primary key of the recipe being commented on.
            reply_to (db.Integer):
                        If this comment is a reply, then store the pk of the
                        comment we are replying to. Otherwise, store None.
            contents (db.String):
                        The contents of this comment. Can be up to 1024
                        characters long.
            uploaded (db.DateTime):
                        The time when this comment was uploaded.
            suggestion (db.Boolean):
                        Is this comment a suggestion?
    """

    pk: int
    uid: int
    recipe_key: int
    reply_to: int
    contents: str
    uploaded: timedelta
    suggestion: bool

    pk = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey("user.uid"), nullable=False)
    recipe_key = db.Column(db.Integer, db.ForeignKey("recipe.pk"),
                           nullable=False)
    reply_to = db.Column(db.Integer, unique=False, nullable=True)
    contents = db.Column(db.String(1024), unique=False, nullable=False)
    uploaded = db.Column(db.DateTime(), unique=False, nullable=False)
    suggestion = db.Column(db.Boolean, unique=False, nullable=False)


@dataclass
class UserInteractionIngredient(InteractionMixin, db.Model):
    """
        This model represents user interactions with ingredients.

        Attributes:
            __tablename__ (str):
                        The name of this user interaction table
                            Set to <tt>user_interaction_ingredient</tt>.
            ingredient_key (db.Integer):
                        The primary key of the ingredient this user is
                            interacting with.
    """

    ingredient_key: int

    __tablename__ = "user_interaction_ingredient"

    ingredient_key = db.Column(db.Integer, db.ForeignKey("ingredient.pk"),
                               nullable=False)


@dataclass
class UserInteractionKitchenware(InteractionMixin, db.Model):
    """
        This model represents user interactions with kitchenware.

        Attributes:
            __tablename__ (str):
                        The name of this user interaction table
                            Set to <tt>user_interaction_kitchenware</tt>.
            kitchenware_key (db.Integer):
                        The primary key of the kitchenware this user is
                            interacting with.
    """

    kitchenware_key: int

    __tablename__ = "user_interaction_kitchenware"

    kitchenware_key = db.Column(db.Integer, db.ForeignKey("kitchenware.pk"),
                                nullable=False)


@dataclass
class UserInteractionRecipe(InteractionMixin, db.Model):
    """
        This model represents user interactions with recipes.

        Attributes:
            __tablename__ (str):
                        The name of this user interaction table
                            Set to <tt>user_interaction_kitchenware</tt>.
            recipe_key (db.Integer):
                        The primary key of the recipe this user is
                            interacting with.
    """

    recipe_key: int

    __tablename__ = "user_interaction_recipe"

    recipe_key = db.Column(db.Integer, db.ForeignKey("recipe.pk"),
                           nullable=False)


@dataclass
class UserInteractionSearch(InteractionMixin, db.Model):
    """
        This model represents user interactions with search terms.

        Attributes:
            __tablename__ (str):
                        The name of this user interaction table
                            Set to <tt>user_interaction_search</tt>.
            search_term (db.String(256)):
                        The search term that a user has input.
    """

    search_term: str

    __tablename__ = "user_interaction_search"

    search_term = db.Column(db.String(256), unique=False, nullable=False)


@dataclass
class UserInteractionProfile(InteractionMixin, db.Model):
    """
        This model represents user A's interactions with user B's profile.

        Attributes:
            __tablename__ (str):
                        The name of this user interaction table
                            Set to <tt>user_interaction_profile</tt>.
            profile_accessed (db.Integer):
                        The primary key of user B whose profile
                            user A has viewed.
    """

    profile_accessed: int

    __tablename__ = "user_interaction_profile"

    profile_accessed = db.Column(db.Integer, db.ForeignKey("user.uid"))
