from flask import render_template


def conflict(e):
    """
        This function handles HTTP error 409.
    """

    return render_template("error/409.html"), 409
