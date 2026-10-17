import unittest

from calculator import add, divide, multiply, subtract


class CalculatorTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-2, 3), -5)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        self.assertAlmostEqual(divide(1, 4), 0.25)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_invalid_operands(self):
        for operation in (add, subtract, multiply, divide):
            with self.subTest(operation=operation.__name__):
                with self.assertRaises(TypeError):
                    operation("1", 2)

    def test_boolean_operands_are_rejected(self):
        for operation in (add, subtract, multiply, divide):
            with self.subTest(operation=operation.__name__):
                with self.assertRaises(TypeError):
                    operation(True, 2)


if __name__ == "__main__":
    unittest.main()
