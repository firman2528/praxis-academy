import unittest

# from class_and_instance import Dog
from oop_objvar import *
from latihan1 import D as d
from latihan2 import *


class TestAll(unittest.TestCase) :
    def testnama(self) :
        truth = d()
        hasil = d.truth(5)
        self.assertEqual(truth, "Bilangan Ganjil")

if __name__ == '__main__' :
    unittest.main()

