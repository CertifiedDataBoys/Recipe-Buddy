from flask import render_template


def im_a_teapot(e):

    return render_template("error/418.html"), 418
