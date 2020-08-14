from flask import Blueprint, render_template, flash, redirect, url_for

from forms import Registration_Form
from models import User

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
        flash("Please login")
        return redirect(url_for("index.index"))
    return render_template("register.html", form=form)
