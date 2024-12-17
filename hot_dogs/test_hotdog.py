import ast
from contextlib import redirect_stdout
import inspect
from io import StringIO
from textwrap import dedent
import unittest

from hotdog import dog_and_bun_packs_needed


class DogAndBunPacksTests(unittest.TestCase):

    """Tests for dog_and_bun_packs_needed function."""

    def test_example_cases(self):
        self.assertEqual(dog_and_bun_packs_needed(7), (1, 1))
        self.assertEqual(dog_and_bun_packs_needed(10), (2, 1))
        self.assertEqual(dog_and_bun_packs_needed(14), (2, 2))
        self.assertEqual(dog_and_bun_packs_needed(20), (3, 2))
        self.assertEqual(dog_and_bun_packs_needed(21), (3, 3))
        self.assertEqual(dog_and_bun_packs_needed(28), (4, 3))

    def test_zero_guests(self):
        self.assertEqual(dog_and_bun_packs_needed(0), (0, 0))

    def test_one_guest(self):
        self.assertEqual(dog_and_bun_packs_needed(1), (1, 1))

    def test_eight_guests(self):
        self.assertEqual(dog_and_bun_packs_needed(8), (1, 1))

    def test_nine_guests(self):
        self.assertEqual(dog_and_bun_packs_needed(9), (2, 1))

    def test_ten_guests(self):
        self.assertEqual(dog_and_bun_packs_needed(10), (2, 1))

    def test_eleven_guests(self):
        self.assertEqual(dog_and_bun_packs_needed(11), (2, 2))

    def test_large_number_of_guests(self):
        self.assertEqual(dog_and_bun_packs_needed(100), (13, 10))

    def test_very_large_number_of_guests(self):
        self.assertEqual(dog_and_bun_packs_needed(1000000), (125000, 100000))

    def test_zreturn_instead_of_print(self):
        with redirect_stdout(StringIO()) as stdout:
            actual = dog_and_bun_packs_needed(8)
        output = stdout.getvalue().strip()
        if actual is None and output:
            self.fail(
                "\n\nUh oh!\n"
                "It looks like you may have printed instead of returning.\n"
                "See https://pym.dev/print-vs-return/\n"
                f"None was returned but this was printed:\n{output}"
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
