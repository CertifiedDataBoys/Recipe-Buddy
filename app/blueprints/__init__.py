"""
    This module is where our Flask blueprints reside.
"""

from . import index, test

ALL_BLUEPRINTS = [
    index.bp,
    test.bp
]
