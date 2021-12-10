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
    food.DietaryRestriction,
    food.RestrictionOnIngredient,
    food.Recipe,
    food.InstructionInRecipe,
    food.InstructionInRecipe,
    food.IngredientInRecipe,
    food.KitchenwareInRecipe,
    food.MediaInRecipe,
    user.User,
    user.UserProfile,
    user.UserDietaryRestriction,
    pantry.PantryIngredient,
    pantry.PantryKitchenware,
    interactions.RecipeRating,
    interactions.RecipeComment,
    interactions.UserInteractionIngredient,
    interactions.UserInteractionKitchenware,
    interactions.UserInteractionRecipe,
    interactions.UserInteractionSearch,
    interactions.UserInteractionProfile
)

DROP_ORDER = (
    interactions.UserInteractionIngredient,     # depends on user.User,
                                                # food.Ingredient

    interactions.UserInteractionRecipe,         # depends on user.User,
                                                # food.Recipe
    interactions.RecipeRating,                  # depends on user.User,
                                                # food.Recipe
    interactions.RecipeComment,                 # depends on user.User,
                                                # food.Recipe

    user.UserDietaryRestriction,               # depends on user.User,
                                                # food.DietaryRestriction

    food.RestrictionOnIngredient,               # depends on food.Ingredient,
                                                # food.DietaryRestriction

    interactions.UserInteractionKitchenware,    # depends on user.User,
                                                # food.Kitchenware

    food.IngredientInRecipe,                    # depends on food.Ingredient,
                                                # food.Recipe

    food.KitchenwareInRecipe,                   # depends on food.Kitchenware,
                                                # food.Recipe

    pantry.PantryIngredient,                    # depends on user.User,
                                                # food.Ingredient

    pantry.PantryKitchenware,                   # depends on user.User,
                                                # food.Kitchenware

    food.InstructionInRecipe,                   # depends on food.Recipe
    food.MediaInRecipe,                         # depends on food.Recipe

    interactions.UserInteractionSearch,         # depends on user.User
    interactions.UserInteractionProfile,        # depends on user.User
    user.UserProfile,                           # depends on user.User

    food.Recipe,
    food.Ingredient,
    food.Kitchenware,
    food.DietaryRestriction,
    user.User
)
