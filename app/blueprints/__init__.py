"""
    This module is where our Flask blueprints reside.
"""

from . import index, recipe, login

ALL_BLUEPRINTS = (
    index.bp,
    recipe.bp,
    login.bp
)
