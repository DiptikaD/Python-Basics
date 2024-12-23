import ast
from contextlib import redirect_stdout
import inspect
from io import StringIO
from textwrap import dedent

import unittest

from format_time import format_time


class FormatTimeTests(unittest.TestCase):

    """Tests for format_time."""

    def test_format_time_single_digit_seconds(self):
        self.assertEqual(format_time(65), "1:05")
        self.assertEqual(format_time(301), "5:01")

    def test_format_time_even_minutes(self):
        self.assertEqual(format_time(120), "2:00")
        self.assertEqual(format_time(600), "10:00")
        self.assertEqual(format_time(180), "3:00")
        self.assertEqual(format_time(3600), "60:00")

    def test_format_time_double_digit_seconds(self):
        self.assertEqual(format_time(75), "1:15")
        self.assertEqual(format_time(119), "1:59")
        self.assertEqual(format_time(3715), "61:55")

    def test_format_time_zero_seconds(self):
        self.assertEqual(format_time(0), "0:00")

    def test_zreturn_instead_of_print(self):
        with redirect_stdout(StringIO()) as stdout:
            actual = format_time(10)
        output = stdout.getvalue().strip()
        if actual is None and output:
            self.fail(
                "\n\nIt looks like you may have printed instead of returning.\n"
                "See https://pym.dev/print-vs-return/\n"
                f"None was returned but this was printed: {output}"
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
