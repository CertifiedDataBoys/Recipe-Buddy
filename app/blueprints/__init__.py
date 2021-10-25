"""
    This module is where our Flask blueprints reside.
"""
from . import index, login, register, recipe, teapot

ALL_BLUEPRINTS = (
    index.bp,
    recipe.bp,
    login.bp,
    register.bp,
    teapot.bp
)
