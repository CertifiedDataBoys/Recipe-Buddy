from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user
from ..forms import LoginForm
from ..models import User


bp = Blueprint("login", __name__)


@bp.route("/login", methods=['GET','POST'])
def login():
    """
        Create a blueprint to handle a test page.
    """

    if current_user.is_authenticated:

        return redirect(url_for('index.index'))


    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):

            flash("Invalid username or password!")
            return redirect(url_for("login.login"))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index.index'))

    return render_template("login.html", title="Login", form=form)


@bp.route("/logout")
def logout():

    logout_user()
    return(redirect(url_for('index.index')))
