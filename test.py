import unittest
from unittest.mock import patch
import App

class TestApp(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(App.addition(2, 3), 5)
        self.assertEqual(App.addition(-1, -1), -2)

    def test_subtraction(self):
        self.assertEqual(App.subtraction(5, 3), 2)
        self.assertEqual(App.subtraction(3, 5), -2)

    @patch('builtins.print')
    def test_main(self, mock_print):
        App.main()
        mock_print.assert_any_call(5)
        mock_print.assert_any_call(2)

if __name__ == "__main__":
    unittest.main()



