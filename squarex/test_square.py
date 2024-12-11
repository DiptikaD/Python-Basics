import ast
from math import sqrt
from numbers import Number
from pathlib import Path
import unittest

import square


class NameTests(unittest.TestCase):

    """Tests for name variable."""

    def test_has_correct_variables(self):
        self.assertTrue(hasattr(square, "x"), "Missing 'x' assignment")
        self.assertTrue(hasattr(square, "y"), "Missing 'y' assignment")

    def test_variables_are_numbers(self):
        self.assertTrue(isinstance(square.x, Number), "x must be a number")
        self.assertTrue(isinstance(square.y, Number), "y must be a number")

    def test_square_root_of_y_is_x(self):
        self.assertEqual(square.x * square.x, square.y, "y must be x squared")
        self.assertAlmostEqual(sqrt(square.y), square.x)

    def test_arithmetic_used(self):
        module_code = Path(square.__file__).read_text()
        node_tree = ast.parse(module_code)
        assignments = {
            node.targets[0].id: node.value
            for node in node_tree.body
            if isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
        }
        self.assertGreater(len(assignments), 1, "File must have 2 assignments")
        self.assertIn("x", assignments, "x must be directly assigned with '='")
        self.assertIn("y", assignments, "y must be directly assigned with '='")
        self.assertFalse(
            isinstance(assignments["y"], ast.Constant),
            "y cannot be assigned to a constant",
        )
        self.assertIn(
            "x",
            ast.unparse(assignments["y"]),
            "y assignment must contain x",
        )


if __name__ == "__main__":
    from platform import python_version
    import sys
    if sys.version_info < (3, 9):
        sys.exit("Running {}.  Python 3.9 required.".format(python_version()))
    unittest.main(verbosity=2)
