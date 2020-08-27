"""
Module containing all the unit tests. Can be run by executing
"python -m unittest" on src directory
"""
import unittest
from datetime import datetime

import app_factory
from models import db, User, Character, Item, Offer, Level


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

            # Creating test characters
            new_character_1 = Character(
                name="Tinemir",
                )
            new_character_1.levels.append(Level(class_="ranger", levels=5))
            new_character_1.levels.append(Level(class_="rogue", levels=4))
            new_character_1.levels.append(Level(class_="fighter", levels=6))

            new_character_2 = Character(
                name="Uther",
            )
            new_character_2.levels.append(Level(class_="cleric", levels=15))

            new_character_3 = Character(
                name="Rosquette",
            )
            new_character_3.levels.append(Level(class_="barbarian", levels=4))
            new_character_3.levels.append(Level(class_="fighter", levels=6))

            # Creating test items
            new_item_1 = Item(
                name="Magic Sword",
                type_="Weapon",
                rarity="Unique",
                attuned=True,
                notes="Bleeds",
                source="DMG"
            )

            new_item_2 = Item(
                name="Magic Staff",
                type_="Weapon",
                rarity="Rare",
                attuned=True,
                notes="Bleeds",
                source="DMG"
            )

            new_item_3 = Item(
                name="Magic beads",
                type_="Weapon",
                rarity="Uncommon",
                attuned=True,
                notes="Bleeds",
                source="DMG"
            )

            # Commiting all objects to DB
            new_character_1.items.append(new_item_1)
            new_character_1.items.append(new_item_2)
            new_character_3.items.append(new_item_3)
            new_user_1.characters.append(new_character_1)
            new_user_1.characters.append(new_character_2)
            new_user_2.characters.append(new_character_3)
            db.session.add(new_user_1)
            db.session.add(new_user_2)
            db.session.commit()

            # Creating Offers
            new_offer_1 = Offer(
                offered_item=new_item_1.item_id,
                wanted_item=new_item_3.item_id,
                date_created=datetime.now(),
            )
            db.session.add(new_offer_1)
            db.session.commit()

    def test_status(self):
        """
        Check if health status page is returning OK
        """
        client = self.app.test_client()
        result = client.get("/healthz")
        self.assertIn(b"OK", result.data)
