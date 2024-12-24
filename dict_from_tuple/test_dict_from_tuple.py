import ast
from contextlib import redirect_stdout
import inspect
from io import StringIO
from textwrap import dedent
import unittest
from dict_from_tuple import dict_from_tuple


class DictFromTupleTests(unittest.TestCase):

    """Tests for dict_from_tuple."""

    def test_four_items(self):
        inputs = [(1, 2, 3, 4), (5, 6, 7, 8)]
        outputs = {1: (2, 3, 4), 5: (6, 7, 8)}
        self.assertEqual(dict_from_tuple(inputs), outputs)

    def test_three_items(self):
        inputs = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        outputs = {1: (2, 3), 4: (5, 6), 7: (8, 9)}
        self.assertEqual(dict_from_tuple(inputs), outputs)

    def test_zreturn_instead_of_print(self):
        with redirect_stdout(StringIO()) as stdout:
            actual = dict_from_tuple([])
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
