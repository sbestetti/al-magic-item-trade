from flask import Blueprint, render_template, flash, redirect, url_for

from sqlalchemy.exc import IntegrityError

from forms import Registration_Form
from models import User, db


bp = Blueprint("register", __name__, url_prefix="/register")


@bp.route("/", methods=["GET", "POST"])
def register():
    form = Registration_Form()
    if form.validate_on_submit():
        user = User()
        user.name = form.name.data
        user.email = form.email.data
        user.dci = form.dci.data
        user.active = True
        user.verified = False
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            flash("User already exists")
            return render_template("register.html", form=form)
        flash("Please login")
        return redirect(url_for("index.index"))
    return render_template("register.html", form=form)
