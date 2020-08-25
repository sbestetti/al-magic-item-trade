from flask import (
    Blueprint,
    render_template,
    flash,
    redirect,
    url_for)

from sqlalchemy.exc import IntegrityError

from forms import Registration_Form
from models import User
from dao import db


bp = Blueprint("register", __name__, url_prefix="/register")


@bp.route("/", methods=["GET", "POST"])
def register():
    form = Registration_Form()
    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            email=form.email.data,
            dci=form.dci.data,
            active=True,
            verified=False
        )
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            flash("User already exists")
            return render_template("register.html", form=form)
        flash("Please login")
        return redirect(url_for("index.index"))
    return render_template("register.html", form=form)
