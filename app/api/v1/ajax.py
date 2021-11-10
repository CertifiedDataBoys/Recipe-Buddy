from flask import abort, Blueprint, render_template, Response, request

bp = Blueprint("api_v1_ajax", __name__)


@bp.route("/api/v1.0.0/public/ajax.js")
def ajax():
    pk = request.args.get("pk")
    page = request.args.get("page")

    if not pk and not page:
        return abort(404);

    return Response(render_template("ajax.j2", pk=pk, page=page), mimetype='text/javascript')
