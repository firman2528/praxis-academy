import unittest
# import ipywidgets as widgets
class WidgetTestCase(unittest.TestCase) :
    def setUp(self) :
        self.widget=Widget('The Widget')

    def tearDown(self) :
        self.widget.dispose()

    def test_default_widget_size(self) :
        self.assetEqual(self.widget.size(), 50,50, 'incorrect default size')

    def test_widget_resize(self) :
        self.widget_resize(100,150)
        self.assertEqual(self.widget.size(), (100,150, 'wrong after resize'))

def suite(self) :
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__' :
    runner = unittest.TextTestRunner()
    runner.run(suite)
    