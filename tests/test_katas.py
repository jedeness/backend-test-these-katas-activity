import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(7, 5), 12)

    def test_multiply(self):
        self.assertEqual(katas.multiply(7, 5), 35)

    def test_power(self):
        self.assertEqual(katas.power(7, 5), 16807)

    def test_factorial(self):
        self.assertEqual(katas.factorial(7), 5040)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(7), 8)


if __name__ == '__main__':
    unittest.main()
