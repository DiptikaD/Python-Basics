import ast
import inspect
from pathlib import Path
from textwrap import dedent
import unittest

from vowels import get_vowel_names


class GetVowelNamesTests(unittest.TestCase):

    """Tests for get_vowel_names."""

    def test_one_vowel_name(self):
        self.assertEqual(
            get_vowel_names(["Alice", "Bob", "Christy", "Jules"]),
            ["Alice"],
        )

    def test_multiple_vowel_names(self):
        self.assertEqual(
            get_vowel_names(["Scott", "arthur", "Jan", "Elizabeth"]),
            ["arthur", "Elizabeth"],
        )

    def test_empty(self):
        self.assertEqual(get_vowel_names([]), [])

    def assertEqual(self, actual, expected, message=None):
        if message:
            return super().assertEqual(actual, expected, message)
        if actual == expected:
            return  # Success!
        function_call = get_actual_function_call(inspect.currentframe().f_back)
        message = dedent(f"""\
            {actual!r} != {expected!r}\n
            Ran:          {function_call}
            Expected:     {expected!r}
            Instead got:  {actual!r}
        """).rstrip("\n")
        if actual is None:
            message += "\n\nDid you forget to return from your function?"
        raise self.failureException(message)


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


if __name__ == "__main__":
    unittest.main(verbosity=2)
