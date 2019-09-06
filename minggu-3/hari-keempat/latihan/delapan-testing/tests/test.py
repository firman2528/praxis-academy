import flaskr
import unittest

class MyTestCase(unittest.TestCase) :
    def setup(self) :
        flaskr.app.testing = True
        self.app = flaskr.app.test_client()

    def test_home(self) :
        result = self.app.get('/')