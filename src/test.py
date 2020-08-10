"""
Module containing all the unit tests. Can be run by executing
"python -m unittest" on src directory
"""
import unittest

import app_factory


class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = app_factory.get_app()

    def test_status(self):
        """
        Check if health status page is returning OK
        """
        client = self.app.test_client()
        result = client.get("/healthz")
        self.assertIn(b"OK", result.data)
