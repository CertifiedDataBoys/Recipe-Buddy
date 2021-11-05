from flask import render_template


def bad_request(e):
    """
        This function handles HTTP error 400.
    """

    return render_template("error/400.html"), 400
