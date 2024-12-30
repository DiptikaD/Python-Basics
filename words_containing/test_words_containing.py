import ast
import inspect
from pathlib import Path
from textwrap import dedent
import unittest

from words_containing import words_containing


class WordsContainingTests(unittest.TestCase):

    """Tests for words_containing."""

    def test_first_letter(self):
        zen_line_2 = ["Explicit", "is", "better", "than", "implicit"]
        self.assertEqual(words_containing(zen_line_2, "b"), ["better"])

    def test_repeated_letter(self):
        zen_line_2 = ["Explicit", "is", "better", "than", "implicit"]
        self.assertEqual(
            words_containing(zen_line_2, "i"),
            ["Explicit", "is", "implicit"],
        )

    # To test bonus 1, comment out the next line
    @unittest.expectedFailure
    def test_case_insensitive(self):
        zen_line_2 = ["Explicit", "is", "better", "than", "implicit"]
        self.assertEqual(
            words_containing(zen_line_2, "e"),
            ["Explicit", "better"],
        )
        self.assertEqual(
            words_containing(zen_line_2, "E"),
            ["Explicit", "better"],
        )

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
    resolver = VariableResolver(caller_frame.f_locals)
    resolved_node = resolver.visit(actual_arg)
    ast.fix_missing_locations(resolved_node)
    return ast.unparse(resolved_node)


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


class VariableResolver(ast.NodeTransformer):
    """AST utility to replace variables with their actual values."""

    def __init__(self, local_vars):
        self.local_vars = local_vars

    def visit_Name(self, node):
        if node.id in self.local_vars:
            value = self.local_vars[node.id]
            if isinstance(value, list):
                return ast.List(
                    elts=[
                        ast.Constant(value=v)
                        for v in value
                    ],
                    ctx=ast.Load(),
                )
            return ast.Constant(value=value)
        return node


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""
    class resultclass(unittest.TextTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=AllowUnexpectedSuccessRunner)
