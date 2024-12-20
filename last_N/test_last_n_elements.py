import unittest
import inspect
import ast
from textwrap import dedent

from last_n_elements import last_n_elements


class LastNElementsTests(unittest.TestCase):

    """Tests for last_n_elements."""

    def test_fruits(self):
        inputs = ["apples", "oranges", "bananas", "strawberries", "pears"]
        outputs = ["bananas", "strawberries", "pears"]
        self.assertEqual(last_n_elements(inputs, 3), outputs)

    def test_last_one(self):
        self.assertEqual(last_n_elements(["apple", "orange", "pear"], 1), ["pear"])

    def test_empty_list(self):
        self.assertEqual(last_n_elements([2, 1, 3, 4, 7, 11], 3), [4, 7, 11])

    def test_zero_items(self):
        self.assertEqual(last_n_elements(["apple", "pear", "grape"], 0), [])

    def test_original_list_is_unchanged(self):
        inputs = [2, 1, 3, 4, 7, 18, 29]
        last_n_elements(inputs, 3)
        self.assertEqual(
            inputs,
            [2, 1, 3, 4, 7, 18, 29],
            "The passed-in list must not be mutated",
        )

    # To test bonus 1, comment out the next line
    @unittest.expectedFailure
    def test_reverse_true(self):
        inputs = ["apple", "orange", "banana", "strawberry", "kiwi"]
        outputs = ["kiwi", "strawberry", "banana"]
        output2 = ["banana", "strawberry", "kiwi"]
        self.assertEqual(last_n_elements(inputs, 3, reverse=True), outputs)
        self.assertEqual(last_n_elements(inputs, 3, reverse=False), output2)

    def assertEqual(self, actual, expected, message=None):
        if message:
            return super().assertEqual(actual, expected, message)
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


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""
    class resultclass(unittest.TextTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=AllowUnexpectedSuccessRunner)
