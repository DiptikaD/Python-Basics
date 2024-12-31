import ast
import inspect
from pathlib import Path
from textwrap import dedent
import unittest

from characters import characters


class BaseTestCase(unittest.TestCase):
    def assertEqual(self, actual, expected):
        if actual == expected:
            return  # Success!
        function_call = get_actual_function_call(inspect.currentframe().f_back)
        message = dedent(f"""
            {actual!r} != {expected!r}\n
            Ran:          {function_call}
            Expected:     {expected!r}
            Instead got:  {actual!r}
        """).strip("\n")
        if actual is None:
            message += "\n\nDid you forget to return from your function?"
        raise self.failureException(message)


class CharactersTests(BaseTestCase):

    """Tests for characters."""

    def test_one_lowercase_word(self):
        self.assertEqual(
            characters("hello"),
            ['h', 'e', 'l', 'l', 'o'],
        )

    def test_letters_are_lowercased(self):
        self.assertEqual(
            characters("Trey Hunner"),
            ['t', 'r', 'e', 'y', ' ', 'h', 'u', 'n', 'n', 'e', 'r'],
        )


# To test bonus 1, comment out the next line
@unittest.expectedFailure
class CharactersSortTests(BaseTestCase):

    """Tests for characters bonus."""

    def test_without_sorting(self):
        self.assertEqual(
            characters("hello", sort=False),
            ['h', 'e', 'l', 'l', 'o'],
        )

    def test_with_sorting(self):
        self.assertEqual(
            characters("hello", sort=True),
            ['e', 'h', 'l', 'l', 'o'],
        )

    def test_lowercasing_and_sorting(self):
        self.assertEqual(
            characters("Trey Hunner", sort=True),
            [' ', 'e', 'e', 'h', 'n', 'n', 'r', 'r', 't', 'u', 'y'],
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
