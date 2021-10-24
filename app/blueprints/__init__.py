"""
    This module is where our Flask blueprints reside.
"""

from . import index, test, login

ALL_BLUEPRINTS = [
    index.bp,
    test.bp,
    login.bp
]
