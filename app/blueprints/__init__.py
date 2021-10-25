"""
    This module is where our Flask blueprints reside.
"""

from . import index, login, recipe, teapot

ALL_BLUEPRINTS = (
    index.bp,
    recipe.bp,
    login.bp,
    teapot.bp
)
