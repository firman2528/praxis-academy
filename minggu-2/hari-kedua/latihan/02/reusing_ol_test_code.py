import unittest

def testsomething() :
    something = makesomething()
    assert something.name is not None


testcase = unittest.FunctionTestCase(testsomething, setup=makeSomethingDB, tearDown=deleteSomethingDB)