import unittest
from src.calculator import func1, func2, func3, func4

class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(func1(2, 3), 5)

    def test_fun2(self):
        self.assertEqual(func2(10, 4), 6)

    def test_fun3(self):
        self.assertEqual(func3(4, 3), 12)

    def test_fun4(self):
        self.assertEqual(func4(2, 3), 10)

if __name__ == '__main__':
    unittest.main()