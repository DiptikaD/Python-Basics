import ast
from collections.abc import Iterable
from contextlib import redirect_stdout
import inspect
from io import StringIO
from pathlib import Path
from textwrap import dedent
import unittest

from split_in_half import split_in_half


class BaseTestCase(unittest.TestCase):
    def assertIterableEqual(self, actual, expected):
        if (
                actual == expected
                or isinstance(actual, Iterable)
                and list(actual) == list(expected)
        ):
            return  # Success!
        function_call = get_actual_function_call(inspect.currentframe().f_back)
        message = dedent(f"""
            {tuple(actual)!r} != {tuple(expected)!r}\n
            Ran:          {function_call}
            Expected:     {tuple(expected)!r}
            Instead got:  {tuple(actual)!r}
        """).strip("\n")
        if actual is None:
            message += "\n\nDid you forget to return from your function?"
        raise self.failureException(message)


class HalfTests(BaseTestCase):

    """Tests for split_in_half."""

    def test_zreturn_instead_of_print(self):
        with redirect_stdout(StringIO()) as stdout:
            actual = split_in_half([1, 2])
        output = stdout.getvalue().strip()
        if actual is None and output:
            self.fail(
                "\n\nIt looks like you may have printed instead of returning.\n"
                "See https://pym.dev/print-vs-return/\n"
                f"None was returned but this was printed: {output}"
            )

    def test_empty(self):
        self.assertIterableEqual(split_in_half([]), ([], []))

    def test_two(self):
        self.assertIterableEqual(split_in_half([1, 2]), ([1], [2]))

    def test_one(self):
        self.assertIterableEqual(split_in_half([1]), ([], [1]))

    def test_even_number_of_items(self):
        self.assertIterableEqual(split_in_half([1, 2, 3, 4]), ([1, 2], [3, 4]))

    def test_odd_number_of_items(self):
        self.assertIterableEqual(
            split_in_half([2, 1, 3, 4, 7, 11, 18]),
            ([2, 1, 3], [4, 7, 11, 18])
        )
        self.assertIterableEqual(
            split_in_half([2, 1, 3, 4, 7]),
            ([2, 1], [3, 4, 7])
        )
        self.assertIterableEqual(split_in_half([2, 1, 3]), ([2], [1, 3]))


# To test bonus 1, comment out the next line
@unittest.expectedFailure
class BonusHalfTests(BaseTestCase):

    """Bonus 1 tests for split_in_half."""

    def test_tuple(self):
        self.assertIterableEqual(split_in_half((1, 2, 3, 4)), ((1, 2), (3, 4)))

    def test_string(self):
        self.assertIterableEqual(
            split_in_half("Hello world!"),
            ('Hello ', 'world!'),
        )


def get_actual_function_call(caller_frame):
    """Use magic to get the actual function call for the assertion."""
    filename = caller_frame.f_code.co_filename
    lineno = caller_frame.f_lineno
    source = Path(filename).read_text()
    visitor = AssertVisitor(lineno)
    visitor.visit(ast.parse(source))
    if visitor.assert_node is None:
        raise RuntimeError("The tests are broken")
    actual_arg = visitor.assert_node.args[0]
    return ast.unparse(actual_arg)


class AssertVisitor(ast.NodeVisitor):
    """AST utility to find self.assert* call at a specific line number."""
    def __init__(self, lineno):
        self.lineno = lineno
        self.assert_node = None

    def visit_Call(self, node):
        if (
                isinstance(node.func, ast.Attribute) and
                node.func.attr.startswith("assert") and
                node.lineno <= self.lineno <= node.end_lineno
        ):
            self.assert_node = node
        self.generic_visit(node)


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""
    class resultclass(unittest.TextTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=AllowUnexpectedSuccessRunner)
