from .database import db
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


class RecipeRating(db.Model):
    """
        This model represents recipe ratings.

        Attributes:
            pk (db.Integer):
                        The primary key of a given user interaction model.
            uid (db.Integer):
                        The uid of the user who left this rating.
            recipe_key (db.Integer):
                        The primary key of the recipe being rated.
            rating (db.Float):
                        What rating did the user give to this recipe?
    """

    pk = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey("user.uid"), nullable=False)
    recipe_key = db.Column(db.Integer, db.ForeignKey("recipe.pk"),
                           nullable=False)
    rating = db.Column(db.Float, nullable=False)


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

    __tablename__ = "user_interaction_ingredient"

    ingredient_key = db.Column(db.Integer, db.ForeignKey("ingredient.pk"),
                               nullable=False)


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

    __tablename__ = "user_interaction_kitchenware"

    kitchenware_key = db.Column(db.Integer, db.ForeignKey("kitchenware.pk"),
                                nullable=False)


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

    __tablename__ = "user_interaction_recipe"

    recipe_key = db.Column(db.Integer, db.ForeignKey("recipe.pk"),
                           nullable=False)


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

    __tablename__ = "user_interaction_search"

    search_term = db.Column(db.String(256), unique=False, nullable=False)


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

    __tablename__ = "user_interaction_profile"

    profile_accessed = db.Column(db.Integer, db.ForeignKey("user.uid"))
