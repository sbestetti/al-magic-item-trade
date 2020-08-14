from flask import Blueprint, render_template, request

from forms import Registration_Form

bp = Blueprint("register", __name__, url_prefix="/register")


@bp.route("/", methods=["GET", "POST"])
def register():
    print(request.form)
    form = Registration_Form()
    if form.validate_on_submit():
        print("Form validated: {request.form[0][0]}")
    else:
        print("Not validated")
    return render_template("register.html", form=form)
