from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from models import User, Item


bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@bp.route("/")
@login_required
def dashboard():
    user = current_user
    return render_template("dashboard.html", user=current_user)
