"""
    This module is where our Flask blueprints reside.
"""
from . import index, login, search, new_recipe, register, teapot, recipe, testing

ALL_BLUEPRINTS = (
    index.bp,
    login.bp,
    search.bp,
    new_recipe.bp,
    register.bp,
    teapot.bp,
    recipe.bp,
    testing.bp
)
