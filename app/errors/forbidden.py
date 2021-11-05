from flask import render_template


def forbidden(e):
    """
        This function handles HTTP error 403.
    """

    return render_template("error/403.html"), 403
