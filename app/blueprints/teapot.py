from flask import abort, Blueprint, render_template


bp = Blueprint("teapot", __name__)


@bp.route("/teapot")
def teapot():
    """
        Render a blueprint for our teapot page.
        This should throw HTTP 418 error.
        This mostly exists to test Flask's built-in error handling, as
            error 418 serves no practical purpose in our application.
        <br><br>
        <center><i>I'm a teapot, not a coffee pot!</i></center>
    """

    abort(418)
