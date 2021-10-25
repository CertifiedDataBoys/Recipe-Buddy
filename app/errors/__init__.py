from . import page_not_found

ALL_ERROR_HANDLERS = (
    (404, page_not_found.page_not_found),
)
