from flask import abort, Blueprint, render_template, Response, request

bp = Blueprint("api_v1_ajax", __name__)


@bp.route("/api/v1.0.0/public/ajax.js")
def ajax():
    return Response(render_template("ajax.j2", args=request.args), mimetype='text/javascript')
