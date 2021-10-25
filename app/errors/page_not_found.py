from flask import render_template


def page_not_found(e):
    """
        This function handles HTTP error 404.
    """

    return render_template("error/404.html"), 404
