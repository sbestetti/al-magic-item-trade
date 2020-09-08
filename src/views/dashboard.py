from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from models import User, Item, Item_Model
from forms import New_Item_Form


bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@bp.route("/")
@login_required
def dashboard():
    items = list()
    for item in current_user.items:
        current_model = Item_Model.query.filter_by(
            item_model_id=item.item_model_id
            ).first()
        items.append(current_model)
    return render_template("dashboard.html", user=current_user, items=items)


@bp.route("/new_item", methods=["POST", "GET"])
@login_required
def new_item():
    item_options = list()
    for item in Item_Model.query.all():
        item_options.append(item.name)
    form = New_Item_Form()
    form.item.choices = item_options
    return render_template("new_item.html", form=form)
