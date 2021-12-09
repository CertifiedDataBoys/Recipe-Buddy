from flask import abort, Blueprint, render_template, request


bp = Blueprint("testing", __name__)


@bp.route("/testing/")
def testing_page():
    """
        Render a blueprint for our test page.
    """

    return render_template("testing.html")


@bp.route("/testing/error/")
def err_page():
    """
        Render a blueprint for an error page with the given error number. <br>
        <tt>err</tt> is a URL argument and should be provided. It defaults to 400.
    """

    err = request.args.get("err")

    if not err:
        err = 400

    try:
        abort(int(err))
    except (LookupError, ValueError):
        abort(400)


@bp.route("/testing/upload_profile_photo")
def upload_profile_photo():

    return render_template("testing_image_uploads.html")


@bp.route("/testing/main_boy")
def main_boy():

    return render_template("index.html")
