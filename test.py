#!/usr/bin/env python3
import unittest

from app import *


class TestFunctions(unittest.TestCase):
    """
    Unit Testing
    """

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        assert '<h1>Weather Forecast Tool</h1>' in response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)

    def test_weather(self):
        response = self.app.post('/weather',
                                 json={"location": "UNKNOWN-NonEXISTENT-LOCATION", "date_from": "2018-06-11",
                                       "date_to": "2018-06-11"})
        assert '<h4>Location: Unknown location</h4>' in response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)

    # executed after each test
    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
