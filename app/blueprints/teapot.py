from flask import abort, Blueprint, render_template


bp = Blueprint("teapot", __name__)


@bp.route("/teapot")
def teapot():

    abort(418)
