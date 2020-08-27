from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from models import Character, Level
from forms import Character_Form
from dao import db


bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@bp.route("/")
@login_required
def dashboard():
    chars = Character.query.filter_by(user=current_user).all()
    return render_template("dashboard.html", characters=chars)


@bp.route("/add_char", methods=["POST", "GET"])
@login_required
def add_char():
    form = Character_Form()
    if form.validate_on_submit():
        char = Character(
            name=form.name.data,
            race=form.race.data,
        )
        level = Level(
            class_=form.main_class.data,
            levels=form.level.data
        )
        char.levels.append(level)
        char.user_id = current_user.user_id
        db.session.add(char)
        db.session.commit()
        return redirect(url_for(".dashboard"))
    return render_template("add_char.html", form=form)
