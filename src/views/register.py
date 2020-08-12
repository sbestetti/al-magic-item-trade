from flask import Blueprint, render_template, request

from forms import Registration_Form

bp = Blueprint("register", __name__, url_prefix="/register")


@bp.route("/")
def register():
    form = Registration_Form(request.form)
    return render_template("register.html", form=form)
