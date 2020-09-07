"""
Module containing all the unit tests. Can be run by executing
"python -m unittest" on src directory
"""
import unittest
from datetime import datetime

import app_factory
from models import db, User, Item_Model, Item


class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = app_factory.get_app()
        with self.app.app_context():
            db.init_app(self.app)
            db.drop_all()
            db.create_all()

            # Creating test users
            new_user_1 = User(
                name="Sergio",
                email="sergio@email.com",
                dci="12345678",
                active=True,
                verified=False,
                last_login=datetime.now()
            )
            new_user_1.set_password("123456")

            new_user_2 = User(
                name="Rosca",
                email="rosca@email.com",
                dci="910111213",
                active=True,
                verified=False,
                last_login=datetime.now()
                )
            new_user_2.set_password("123456")

            # Creating test item models
            new_item_model_1 = Item_Model(
                name="Magic Sword",
                type_="Weapon",
                rarity="Unique",
                attuned=True,
                notes="Bleeds",
                source="DMG",
            )

            new_item_model_2 = Item_Model(
                name="Magic Staff",
                type_="Weapon",
                rarity="Rare",
                attuned=True,
                notes="Bleeds",
                source="DMG",
            )

            new_item_model_3 = Item_Model(
                name="Magic beads",
                type_="Weapon",
                rarity="Uncommon",
                attuned=True,
                notes="Bleeds",
                source="DMG",
            )

            # Creating test items
            new_item_1 = Item(
                user=new_user_1,
                item_model=new_item_model_1
            )
            new_item_2 = Item(
                user=new_user_1,
                item_model=new_item_model_2
            )
            new_item_3 = Item(
                user=new_user_2,
                item_model=new_item_model_3
            )

            # Commiting all objects to DB
            db.session.add_all(
                [
                    new_user_1,
                    new_user_2,
                    new_item_model_1,
                    new_item_model_2,
                    new_item_model_3,
                    new_item_1,
                    new_item_2,
                    new_item_3,
                ]
            )
            db.session.commit()

            # Creating Offers
            # new_offer_1 = Offer(
            #     offered_item=new_item_1.item_id,
            #     wanted_item=new_item_3.item_id,
            #     date_created=datetime.now(),
            # )
            # db.session.add(new_offer_1)
            # db.session.commit()

    def test_status(self):
        """
        Check if health status page is returning OK
        """
        client = self.app.test_client()
        result = client.get("/healthz")
        self.assertIn(b"OK", result.data)
