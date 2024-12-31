import ast
import inspect
from textwrap import dedent
import unittest

from len_or_none import len_or_none


class LenOrNoneTests(unittest.TestCase):

    """Tests for len_or_none."""

    def test_hello_string(self):
        self.assertEqual(len_or_none("hello"), 5)

    def test_4(self):
        self.assertIsNone(len_or_none(4))

    def test_empty_list(self):
        self.assertEqual(len_or_none([]), 0)

    def test_range(self):
        self.assertEqual(len_or_none(range(10)), 10)

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
    call_line = inspect.getframeinfo(caller_frame).code_context[0].strip()
    parsed_ast = ast.parse(call_line)
    for node in ast.walk(parsed_ast):
        if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "assertEqual"
        ):
            [actual, expected] = node.args
            return ast.unparse(actual)
    raise RuntimeError("The tests are broken")


if __name__ == "__main__":
    unittest.main(verbosity=2)
