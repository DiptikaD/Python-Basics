import ast
from copy import deepcopy
import inspect
from textwrap import dedent
import unittest

from negate import negate


class NegateTests(unittest.TestCase):

    """Tests for negate."""

    def test_empty(self):
        self.assertEqual(negate([[]]), [[]])

    def test_single_item(self):
        self.assertEqual(negate([[5]]), [[-5]])

    def test_two_by_two_matrix(self):
        inputs = [[1, 2], [3, 4]]
        outputs = [[-1, -2], [-3, -4]]
        self.assertEqual(negate(inputs), outputs)

    def test_two_by_three_matrix(self):
        inputs = [[1, 2, 3], [4, 5, 6]]
        outputs = [[-1, -2, -3], [-4, -5, -6]]
        self.assertEqual(negate(inputs), outputs)

    def test_three_by_two_matrix(self):
        inputs = [[1, 2], [3, 4], [5, 6]]
        outputs = [[-1, -2], [-3, -4], [-5, -6]]
        self.assertEqual(negate(inputs), outputs)

    def test_three_by_three_matrix(self):
        inputs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        outputs = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        self.assertEqual(negate(inputs), outputs)

    def test_negative_numbers(self):
        inputs = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
        outputs = [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]
        self.assertEqual(negate(inputs), outputs)

    def test_input_unchanged(self):
        inputs = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
        original = deepcopy(inputs)
        negated_matrix = negate(inputs)
        self.assertIsNot(inputs, negated_matrix)
        self.assertEqual(inputs, original)

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
    local_vars = caller_frame.f_locals
    call_line = inspect.getframeinfo(caller_frame).code_context[0].strip()
    parsed = ast.parse(call_line)
    for node in ast.walk(parsed):
        if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "assertEqual"
        ):
            [actual, expected] = node.args
            break
    else:
        raise RuntimeError("The tests are broken")
    resolver = VariableResolver(local_vars)
    resolved_call = resolver.visit(actual)
    ast.fix_missing_locations(resolved_call)
    return ast.unparse(resolved_call)


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


if __name__ == "__main__":
    unittest.main(verbosity=2)
