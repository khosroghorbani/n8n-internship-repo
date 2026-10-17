import unittest

from calculator import add, divide, multiply, subtract


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertEqual(subtract(-2, 3), -5)

    def test_multiply(self):
        self.assertEqual(multiply(6, 5), 30)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(1, 4), 0.25)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_operations_reject_non_numeric_operands(self):
        operations = (add, subtract, multiply, divide)
        for operation in operations:
            with self.subTest(operation=operation.__name__):
                with self.assertRaises(TypeError):
                    operation("10", 2)

    def test_operations_reject_boolean_operands(self):
        operations = (add, subtract, multiply, divide)
        for operation in operations:
            with self.subTest(operation=operation.__name__):
                with self.assertRaises(TypeError):
                    operation(True, 2)


if __name__ == "__main__":
    unittest.main()
