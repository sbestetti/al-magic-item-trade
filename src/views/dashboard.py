from flask import Blueprint, render_template

from flask_login import login_required, current_user
from models import Character

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@bp.route("/")
@login_required
def dashboard():
    chars = Character.query.filter_by(user=current_user).all()
    return render_template("dashboard.html", characters=chars)
