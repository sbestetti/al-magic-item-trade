"""
Module containing all the unit tests. Can be run by executing
"python -m unittest" on src directory
"""
import unittest
from datetime import datetime

import start
from models import db, User
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
                dci="1234",
                active=True,
                verified=True,
                last_login=datetime.now(),
                authenticated=False
            )
            test_user_1.set_password("123456")

            test_user_2 = User(
                name="Test User 2",
                email="test2@email.com",
                dci="5678",
                active=True,
                verified=True,
                last_login=datetime.now(),
                authenticated=False
            )
            test_user_2.set_password("123456")

            db.session.add(test_user_1)
            db.session.add(test_user_2)
            db.session.commit()

            self.test_user_1 = User.query.filter_by(user_id=1).first()
            self.test_user_2 = User.query.filter_by(user_id=2).first()

    def test_status(self):
        """
        Check if health status page is returning OK
        """
        client = self.app.test_client()
        result = client.get("/healthz")
        self.assertIn(b"OK", result.data)

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
            # Test representation
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

    def test_index_page(self):
        response = self.test_client.get("/")
        self.assertIn(
            b"Welcome to Adventure League's Magic Item trade",
            response.data
            )

    def test_dashboard_page(self):
        credentials = dict(
            email="test1@email.com",
            password="123456"
        )
        response = self.test_client.post(
            "/",
            data=credentials,
            follow_redirects=True
            )
        self.assertIn(b"Welcome Test User 1", response.data)
