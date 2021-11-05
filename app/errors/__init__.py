"""
    This module is where our Flask error handlers reside.
"""
from . import (
    bad_request, conflict, forbidden, page_not_found, teapot
)


ALL_ERROR_HANDLERS = (
    (400, bad_request.bad_request),
    (403, forbidden.forbidden),
    (404, page_not_found.page_not_found),
    (409, conflict.conflict),
    (418, teapot.im_a_teapot)
)
