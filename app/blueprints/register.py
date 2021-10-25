from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user
from ..forms import RegisterForm
from ..models import User


bp = Blueprint("register", __name__)


@bp.route("/register", methods=['GET','POST'])
def register():
    """
        Create a blueprint to handle a test page.
    """

    if current_user.is_authenticated:

        return redirect(url_for('index.index'))


    form = RegisterForm()

    if form.validate_on_submit():

        if form.username.data and form.email.data and form.password.data:
            user = User(username=form.username.data, email=form.email.data, verified=False)
            user.set_password(form.password.data)
            # Need to add user to database, then send verification email
            # Either use this somehow or make a new function to do it within the db module
            # db.session.add(user)
            # db.session.commit()
            flash("User account created, please verify your email in order to login")
            return redirect(url_for("register.register"))

    return render_template("register.html", title="Login", form=form)
