"""
    This module is where our Flask error handlers reside.
"""
from . import page_not_found, teapot

ALL_ERROR_HANDLERS = (
    (404, page_not_found.page_not_found),
    (418, teapot.im_a_teapot)
)
