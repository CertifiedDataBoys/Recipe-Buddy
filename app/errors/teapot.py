from flask import render_template


def im_a_teapot(e):
    """
        This function handles HTTP error 418.
        This mostly exists to test Flask's built-in error handling, as
            error 418 serves no practical purpose in our application.
        <br><br>
        <center><i>I'm a teapot, not a coffee pot!</i></center>
    """

    return render_template("error/418.html"), 418
