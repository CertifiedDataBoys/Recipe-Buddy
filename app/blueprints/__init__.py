"""
    This module is where our Flask blueprints reside.
"""
from . import index, login, register, teapot, recipe, testing

ALL_BLUEPRINTS = (
    index.bp,
    login.bp,
    register.bp,
    teapot.bp,
    recipe.bp,
    testing.bp
)
