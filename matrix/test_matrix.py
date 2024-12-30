import ast
import inspect
from pathlib import Path
from pprint import pformat
from textwrap import dedent
import unittest

from matrix import matrix_from_string


class MatrixFromStringTests(unittest.TestCase):

    """Tests for matrix_from_string."""

    def test_floating_point_numbers(self):
        self.assertEqual(matrix_from_string("8.5\n7.6"), [[8.5], [7.6]])

    def test_two_by_two_matrix(self):
        self.assertEqual(matrix_from_string("1 2\n10 20"), [[1, 2], [10, 20]])

    def test_three_by_two_matrix(self):
        self.assertEqual(
            matrix_from_string("9 8 7\n19 18 17"),
            [[9, 8, 7], [19, 18, 17]],
        )

    def test_extra_newline(self):
        self.assertEqual(
            matrix_from_string("9 8 7\n19 18 17\n"),
            [[9, 8, 7], [19, 18, 17]],
        )

    # To test bonus 1, comment out the next line
    @unittest.expectedFailure
    def test_lots_of_space(self):
        self.assertEqual(
            matrix_from_string(dedent("""
                 1  5  8 10

                11  2  6  9

                14 12  3  7

                16 15 13  4
            """)),
            [
                [ 1,  5,  8, 10],
                [11,  2,  6,  9],
                [14, 12,  3,  7],
                [16, 15, 13,  4],
            ],
        )
        self.assertEqual(
            matrix_from_string("1  5\n  \n \n3 4"),
            [[1, 5], [3, 4]],
        )

    def assertEqual(self, actual, expected):
        if actual == expected:
            return  # Success!
        function_call = get_actual_function_call(inspect.currentframe().f_back)
        message = dedent(f"""\
            {actual!r} != {expected!r}\n
            Ran:
            {function_call}
        """).rstrip("\n")
        message += f"\n\nExpected:\n{pformat(expected)}"
        message += f"\n\nInstead got:\n{pformat(actual)}"
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
    return unparse(actual_arg)


class Unparser(ast._Unparser):
    """Unparser that maintains multiline string formatting."""

    def visit_Constant(self, node):
        if isinstance(node.value, str) and node.lineno < node.end_lineno:
            super()._write_str_avoiding_backslashes(node.value)
            return
        return super().visit_Constant(node)


def unparse(ast_node):
    return Unparser().visit(ast_node)


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
