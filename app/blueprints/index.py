from flask import Blueprint, render_template
import os

bp = Blueprint("index", __name__)

@bp.route("/")
def index():

    return render_template("index.html", os=os)
