"""
    This module is where v1 of RecipeBuddy's RESTful API resides.
"""
from . import recipe, user

ALL_API_V1_BLUEPRINTS = (
    recipe.bp,
    user.bp
)
