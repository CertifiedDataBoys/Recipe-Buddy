"""
    This module is where v1 of RecipeBuddy's RESTful API resides.
"""
from . import ajax, food, interactions, recipe, user

ALL_API_V1_BLUEPRINTS = (
    ajax.bp,
    food.bp,
    interactions.bp,
    recipe.bp,
    user.bp
)
