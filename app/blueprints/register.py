from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user
from .. import security
from ..forms import RegisterForm
from ..models import db, User


bp = Blueprint("register", __name__)


@bp.route("/register", methods=['GET','POST'])
def register():
    """
        Create a blueprint to handle a registration page.
    """

    if current_user.is_authenticated:

        return redirect(url_for('index.index'))


    form = RegisterForm()

    if form.validate_on_submit():

        if form.username.data and form.email.data and form.password.data:

            # Does a user with this username and / or email exist already?
            if security.register.username_exists(form.username.data) \
               or security.register.email_exists(form.email.data):

                flash("There is already a user with that username or email.")
                return redirect(url_for("register.register"))

            user = User(username=form.username.data, email=form.email.data, verified=True)
            user.set_password(form.password.data)
            # Need to add user to database, then send verification email
            # ... Maybe. We'll get to email verification later.
            security.register.register_user(db, user)
            flash("User account created, please verify your email in order to login")
            return redirect(url_for("register.register"))

    return render_template("register.html", title="Login", form=form)
