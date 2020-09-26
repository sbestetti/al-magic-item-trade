from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models import Offer

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@bp.route("/")
@login_required
def dashboard():
    sent_offers = Offer.query.filter_by(sending_user=current_user).all()
    received_offers = Offer.query.filter_by(receiving_user=current_user).all()
    return render_template(
        "dashboard.html",
        user=current_user,
        sent_offers=sent_offers,
        received_offers=received_offers
        )


@bp.route("/trade_form")
@login_required
def trade_form():
    return render_template("trade_form.html")
