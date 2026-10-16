import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "math.utils.py"
SPEC = importlib.util.spec_from_file_location("math_utils", MODULE_PATH)
math_utils = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(math_utils)


class FactorialTests(unittest.TestCase):
    def test_factorial_returns_expected_values(self):
        self.assertEqual(math_utils.factorial(0), 1)
        self.assertEqual(math_utils.factorial(1), 1)
        self.assertEqual(math_utils.factorial(5), 120)

    def test_factorial_rejects_invalid_values(self):
        for value in (-1, 1.5, "5", True):
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                    ValueError, "n must be a non-negative integer"
                ):
                    math_utils.factorial(value)


if __name__ == "__main__":
    unittest.main()
