"""
    This module is where our Flask models reside.
"""

from .database import db
from .food import *
from .user import *
from .pantry import *
from .interactions import *


ALL_TABLES = (
    food.Ingredient,
    food.Kitchenware,
    food.Recipe,
    food.IngredientInRecipe,
    user.User,
    user.UserProfile,
    pantry.PantryIngredient,
    pantry.PantryKitchenware,
    interactions.UserInteractionIngredient,
    interactions.UserInteractionRecipe,
    interactions.UserInteractionSearch,
    interactions.UserInteractionProfile
)

DROP_ORDER = (
    interactions.UserInteractionIngredient,     # depends on user.User,
                                                # food.Ingredient

    interactions.UserInteractionRecipe,         # depends on user.User,
                                                # food.Recipe

    interactions.UserInteractionKitchenware,    # depends on user.User,
                                                # food.Kitchenware

    food.IngredientInRecipe,                    # depends on food.Ingredient,
                                                # food.Recipe

    food.KitchenwareInRecipe,                   # depends on food.Kitchenware,
                                                # food.Recipe

    pantry.PantryIngredient,                    # depends on user.User,
                                                # food.Ingredient

    pantry.PantryKitchenware,

    interactions.UserInteractionSearch,         # depends on user.User
    interactions.UserInteractionProfile,        # depends on user.User
    user.UserProfile,                           # depends on user.User

    food.Recipe,
    food.Ingredient,
    food.Kitchenware,
    user.User
)
