import unittest

test_cases = [TestCase1, TestCase2, TestCase3]

def load_tests(loader, test, pattern) :
    suite = TestSuite()
    for test_class ini test_cases :
        tests = loader.loadTestFromTestCase(test_class)
        suite.addTests(tests)

    return suite

