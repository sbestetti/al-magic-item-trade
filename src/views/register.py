from flask import Blueprint, render_template, flash, redirect, url_for

from sqlalchemy.exc import IntegrityError

from forms import Registration_Form
from models import User
from dao import add_user


bp = Blueprint("register", __name__, url_prefix="/register")


@bp.route("/", methods=["GET", "POST"])
def register():
    form = Registration_Form()
    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            email=form.email.data,
            dci=form.dci.data,
            password=form.password.data,
            active=True,
            verified=False
        )
        try:
            add_user(user)
        except IntegrityError:
            flash("User already exists")
            return render_template("register.html", form=form)
        flash("Please login")
        return redirect(url_for("index.index"))
    return render_template("register.html", form=form)
