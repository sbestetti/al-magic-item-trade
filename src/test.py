"""
Module containing all the unit tests. Can be run by executing
"python -m unittest" on src directory
"""
import unittest
from datetime import datetime

import start
from models import db, User, Offer, Item, Wanted_Item
import login


class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = start.application
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.context = self.app.app_context()
        self.test_client = self.app.test_client()
        with self.context:
            db.init_app(self.app)
            db.drop_all()
            db.create_all()

            test_user_1 = User(
                name="Test User 1",
                email="test1@email.com",
                dci="123456",
                active=True,
                verified=True,
                last_login=datetime.now(),
                authenticated=False
            )
            test_user_1.set_password("123456")

            test_user_2 = User(
                name="Test User 2",
                email="test2@email.com",
                dci="567890",
                active=True,
                verified=True,
                last_login=datetime.now(),
                authenticated=False
            )
            test_user_2.set_password("123456")

            test_item_1 = Item(
                name="Teste Item 1",
                table="a",
                type_="sword",
                rarity="common",
                attuned=True,
                source="dmg"
            )
            test_item_2 = Item(
                name="Teste Item 2",
                table="a",
                type_="shield",
                rarity="rare",
                attuned=False,
                source="dmg"
            )
            test_item_3 = Item(
                name="Teste Item 3",
                table="b",
                type_="cloak",
                rarity="common",
                attuned=True,
                source="dmg"
            )
            test_item_4 = Item(
                name="Teste Item 4",
                table="b",
                type_="tome",
                rarity="rare",
                attuned=False,
                source="dmg"
            )

            test_offer_1 = Offer(
                date_created=datetime.now(),
                status="pending",
                sending_user=test_user_1,
                receiving_user=test_user_2,
                offered_item=test_item_1,
            )

            test_offer_2 = Offer(
                date_created=datetime.now(),
                status="pending",
                sending_user=test_user_2,
                receiving_user=test_user_1,
                offered_item=test_item_3,
            )

            test_wanted_item_1 = Wanted_Item(
                offer=test_offer_1,
                item=test_item_2
            )

            test_wanted_item_2 = Wanted_Item(
                offer=test_offer_1,
                item=test_item_4
            )

            test_wanted_item_3 = Wanted_Item(
                offer=test_offer_2,
                item=test_item_3
            )

            db.session.add(test_item_1)
            db.session.add(test_item_2)
            db.session.add(test_item_3)
            db.session.add(test_item_4)
            db.session.add(test_user_1)
            db.session.add(test_user_2)
            db.session.add(test_offer_1)
            db.session.add(test_offer_2)
            db.session.add(test_wanted_item_1)
            db.session.add(test_wanted_item_2)
            db.session.add(test_wanted_item_3)
            db.session.commit()

            self.test_user_1 = User.query.filter_by(user_id=1).first()
            self.test_user_2 = User.query.filter_by(user_id=2).first()

    # --------------- Page tests ---------------
    def test_status(self):
        """
        Check if health status page is returning OK
        """
        client = self.app.test_client()
        result = client.get("/healthz")
        self.assertIn(b"OK", result.data)

    def test_index_page(self):
        response = self.test_client.get("/")
        self.assertIn(
            b"Welcome to Adventure League's Magic Item trade",
            response.data
            )

    def test_registration_page(self):
        response = self.test_client.get("/register", follow_redirects=True)
        self.assertIn(
            b"Registration page",
            response.data
            )

    # --------------- Users tests ---------------
    def test_login_module(self):
        """
        Check if the function used by the flask-login plugin
        is working correctly
        """
        with self.context:
            control_user = login.load_user("test1@email.com")
            self.assertEqual(control_user.user_id, self.test_user_1.user_id)

    def test_user_repr(self):
        """
        Test User's class representation
        """
        with self.context:
            expected_repr = "<USER> 1: test1@email.com"
            self.assertTrue(self.test_user_1.__repr__() == expected_repr)

    def test_user_password_methods(self):
        """
        Test User's class password setter and getter
        """
        with self.context:
            self.test_user_1.set_password("test_password")
            self.assertTrue(self.test_user_1.check_password("test_password"))

    def test_user_active_method(self):
        """
        Test User's class method to check if the user
        is active
        """
        with self.context:
            self.assertTrue(self.test_user_1.is_active())

    def test_user_get_id_method(self):
        """
        Test User's class method to return user's
        email
        """
        with self.context:
            self.assertEqual(self.test_user_1.get_id(), "test1@email.com")

    def test_user_authenticated_method(self):
        """
        Test User's class authenticated function
        """
        with self.context:
            self.assertFalse(self.test_user_1.is_authenticated())

    def test_user_is_anonymous_method(self):
        """
        Test User's class anonymous function
        Should always be negative
        """
        with self.context:
            self.assertFalse(self.test_user_1.is_anonymous())

    # --------------- Login tests ---------------
    def test_login_correct(self):
        credentials = dict(
            email="test1@email.com",
            password="123456"
        )
        response = self.test_client.post(
            "/",
            data=credentials,
            follow_redirects=True
            )
        self.assertIn(b"Hello Test User 1", response.data)

    def test_login_incorrect(self):
        credentials = dict(email="test1@email.com", password="wrong_password")
        response = self.test_client.post(
            "/",
            data=credentials,
            follow_redirects=True
            )
        self.assertIn(b"Wrong username or password", response.data)

    def test_logout(self):
        credentials = dict(email="test1@email.com", password="123456")
        self.test_client.post("/", data=credentials, follow_redirects=True)
        response = self.test_client.get("/logout", follow_redirects=True)
        self.assertIn(
            b"Welcome to Adventure League's Magic Item trade",
            response.data
            )

    # --------------- User registration test ---------------
    def test_user_registration_success(self):
        user_data = dict(
            name="Test User 3",
            email="test3@email.com",
            dci="901234",
            password="123456",
            confirm_password="123456"
        )
        response = self.test_client.post(
            "/register",
            data=user_data,
            follow_redirects=True
        )
        self.assertIn(b"Registration successful. Please login", response.data)

    def test_user_registration_user_already_exists(self):
        user_data = dict(
            name="Test User 1",
            email="test1@email.com",
            dci="123456",
            password="123456",
            confirm_password="123456"
        )
        response = self.test_client.post(
            "/register",
            data=user_data,
            follow_redirects=True
        )
        self.assertIn(b"User already exists", response.data)
