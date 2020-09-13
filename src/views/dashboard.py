from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from models import User, Item, Item_Model
from forms import New_Item_Form
from dao import db


bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@bp.route("/")
@login_required
def dashboard():
    """
    This function generates an intermediary object combining the item ID
    and the information from the item model to create rows on the Items table
    """
    items = list()
    for item in current_user.items:
        current_model = Item_Model.query.filter_by(
            item_model_id=item.item_model_id
            ).first()
        table_item = {
            "model": current_model,
            "item_id": item.item_id
        }
        items.append(table_item)
    return render_template("dashboard.html", user=current_user, items=items)


@bp.route("/new_item", methods=["POST", "GET"])
@login_required
def new_item():
    item_options = list()
    for item in Item_Model.query.all():
        item_options.append(item.name)
    form = New_Item_Form()
    form.item.choices = item_options
    if form.validate_on_submit():
        item_model = Item_Model.query.filter_by(name=form.item.data).first()
        new_item = Item(
            character=form.character.data,
            user=current_user,
            item_model=item_model
        )
        db.session.add(new_item)
        db.session.commit()
        flash("Item created")
        return redirect(url_for("dashboard.dashboard"))
    return render_template("new_item.html", form=form)


@bp.route("/trade-item/<item_id>")
@login_required
def trade_item(item_id):
    return f"Your item is {item_id}", 200
