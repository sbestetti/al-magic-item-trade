from flask import Blueprint, render_template, redirect, url_for, flash

from flask_login import login_user, logout_user, login_required, current_user

from forms import Login_Form
from models import User
from dao import db

bp = Blueprint("index", __name__, url_prefix="/")


@bp.route("/", methods=["GET", "POST"])
def index():
    form = Login_Form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for("dashboard.dashboard"))
        else:
            flash("Wrong username or password")
    return render_template("index.html", form=form)


@bp.route("/logout")
@login_required
def logout():
    current_user.authenticated = False
    db.session.add(current_user)
    db.session.commit()
    logout_user()
    return redirect(url_for(".index"))
