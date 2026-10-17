import unittest

import calculator


class CalculatorOperationTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-2, 0.5), -1.5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 4), 6)
        self.assertEqual(calculator.subtract(-2, 3), -5)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(6, 7), 42)
        self.assertEqual(calculator.multiply(-2, 2.5), -5.0)

    def test_divide(self):
        self.assertEqual(calculator.divide(8, 2), 4)
        self.assertAlmostEqual(calculator.divide(1, 3), 1 / 3)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaisesRegex(ZeroDivisionError, "cannot divide by zero"):
            calculator.divide(10, 0)

    def test_operations_reject_invalid_operands(self):
        operations = (
            calculator.add,
            calculator.subtract,
            calculator.multiply,
            calculator.divide,
        )
        invalid_values = ("2", None, True, False, object())

        for operation in operations:
            for invalid_value in invalid_values:
                with self.subTest(
                    operation=operation.__name__, value=invalid_value
                ):
                    with self.assertRaisesRegex(
                        TypeError, "operands must be real numbers"
                    ):
                        operation(invalid_value, 2)

            with self.subTest(operation=operation.__name__, invalid_value="right"):
                with self.assertRaisesRegex(
                    TypeError, "operands must be real numbers"
                ):
                    operation(2, "2")


if __name__ == "__main__":
    unittest.main()
