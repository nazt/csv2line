import unittest
import taprunner


class SimplisticTest(unittest.TestCase):

    def test(self):
        self.assertTrue("A", "A")

    def test2(self):
        self.assertTrue("A", "A")


if __name__ == '__main__':
    # output='test-reports'
    unittest.main(testRunner=taprunner.TAPTestRunner())
