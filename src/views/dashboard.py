from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models import Offer

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@bp.route("/")
@login_required
def dashboard():
    """
    This function generates an intermediary object combining the item ID
    and the information from the item model to create rows on the Items table
    """
    sent_offers = Offer.query.filter_by(sending_user=current_user).all()
    received_offers = Offer.query.filter_by(receiving_user=current_user).all()
    return render_template(
        "dashboard.html",
        user=current_user,
        sent_offers=sent_offers,
        received_offers=received_offers
        )


# @bp.route("/new_item", methods=["POST", "GET"])
# @login_required
# def new_item():
#     item_options = list()
#     for item in Item_Model.query.all():
#         item_options.append(item.name)
#     form = New_Item_Form()
#     form.item.choices = item_options
#     if form.validate_on_submit():
#         item_model = Item_Model.query.filter_by(name=form.item.data).first()
#         new_item = Item(
#             character=form.character.data,
#             user=current_user,
#             item_model=item_model
#         )
#         db.session.add(new_item)
#         db.session.commit()
#         flash("Item created")
#         return redirect(url_for("dashboard.dashboard"))
#     return render_template("new_item.html", form=form)


# @bp.route("/trade-item/<item_id>")
# @login_required
# def trade_item(item_id):
#     """
#     First checks if the selected magic item belongs to
#     the current logged user.
#     """
#     item = Item.query.filter_by(item_id=item_id).first()
#     if item.user == current_user:
#         possible_items = Item_Model.query.filter_by(
#             table=item.item_model.table,
#             rarity=item.item_model.rarity
#             ).all()
#         return render_template("possible_items.html", items=possible_items)
#     else:
#         return "This items doesn't belong to your user.", 200
