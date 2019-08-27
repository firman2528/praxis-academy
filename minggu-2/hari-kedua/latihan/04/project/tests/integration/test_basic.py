from kivy.app import App
import unittest


class TestBasic(unittest.TestCase) :
    def setup(self) :
        # load test data
        self.app = App(database='fixtures/test_basic.json')

    def test_customer_count(self) :
        self.assertEqual(len(self.app.customer),100)

    def test_existence_of_customer(self) :
        customer = self.app.get_customer(id=10)
        self.assertEqual(customer.name, "Org XYZ")
        self.assertEqual(customer.address, "10 Red Road, Reading")


class TestComplexData(unittest.TestCase) :
    def setUp(self) :
        # load test data
        self.app = App(database='fixtures/test_complex.json')

    def test_customer_count(self) :
        self.assertEqual(len(self.app.customer), 10000)

    def test_existence_of_customer(self) :
        customer = self.app.get_customer(id=9999)
        self.assertEqual(customer.name, u"バナナ")
        self.assertEqual(customer.address, "10 Red Road, Akihabara, Tokyo")

if __name__=='__main__' :
    unittest.main()
