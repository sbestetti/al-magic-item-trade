from flask import Flask, jsonify

from models import db


def get_app():
    app = Flask(__name__)
    app.config.from_pyfile("./settings.py")

    db.init_app(app)

    @app.route("/healthz")
    def healthz():
        return jsonify({
            "Status": "OK"
        }), 200

    return app


# @app.route("/run_tests")
# def run_tests():
#     # TODO: Move when tests setup
#     # Tests
#     try:
#         db.drop_all()
#         db.create_all()
#     except Exception as e:
#         return f"Error creating DB: {e}", 500
#     from datetime import datetime

#     from models import User, Character, Item, Offer

#     new_user_1 = User(
#         name="Sergio",
#         email="sergio@email.com",
#         dci="12345678",
#         active=True,
#         verified=False,
#         last_login=datetime.now()
#         )

#     new_user_2 = User(
#         name="Rosca",
#         email="rosca@email.com",
#         dci="910111213",
#         active=True,
#         verified=False,
#         last_login=datetime.now()
#         )

#     new_character_1 = Character(
#         name="Tinemir",
#         )

#     new_character_2 = Character(
#         name="Uther",
#     )

#     new_character_3 = Character(
#         name="Rosquette",
#     )

#     new_item_1 = Item(
#         name="Magic Sword",
#         type_="Weapon",
#         rarity="Unique",
#         attuned=True,
#         notes="Bleeds",
#         source="DMG"
#     )

#     new_item_2 = Item(
#         name="Magic Staff",
#         type_="Weapon",
#         rarity="Rare",
#         attuned=True,
#         notes="Bleeds",
#         source="DMG"
#     )

#     new_item_3 = Item(
#         name="Magic beads",
#         type_="Weapon",
#         rarity="Uncommon",
#         attuned=True,
#         notes="Bleeds",
#         source="DMG"
#     )

#     new_character_1.items.append(new_item_1)
#     new_character_1.items.append(new_item_2)

#     new_character_3.items.append(new_item_3)

#     new_user_1.characters.append(new_character_1)
#     new_user_1.characters.append(new_character_2)
#     new_user_2.characters.append(new_character_3)

#     db.session.add(new_user_1)
#     db.session.add(new_user_2)

#     db.session.commit()

#     # Offer tests
#     new_offer_1 = Offer(
#         offered_item=new_item_1.item_id,
#         wanted_item=new_item_3.item_id,
#         date_created=datetime.now(),
#     )

#     db.session.add(new_offer_1)
#     db.session.commit()

#     # Query tests

#     # Characters by user
#     my_chars = Character.query.filter_by(user=new_user_2).all()
#     print(my_chars)

#     # Items for all characters of a specifc user
#     items = list()
#     for char in my_chars:
#         for item in char.items:
#             items.append(item)

#     # Items with offers
#     offers = list()
#     for i in items:
#         _ = Offer.query.filter_by(wanted_item=i.item_id).all()
#         offers.append(_)
#     print(offers)

#     return "Finished", 200
