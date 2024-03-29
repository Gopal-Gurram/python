import unittest
import main


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'gjakllala'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)


unittest.main()
