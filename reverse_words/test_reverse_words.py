import ast
import inspect
from textwrap import dedent
import unittest

from reverse_words import reverse_words


class ReverseWordOrderTests(unittest.TestCase):

    """Tests for reverse_words."""

    def test_three_words(self):
        self.assertEqual(reverse_words("who is this"), "this is who")

    def test_four_words(self):
        input_sentence = "words some are these"
        output_sentence = "these are some words"
        self.assertEqual(reverse_words(input_sentence), output_sentence)

    def test_one_word(self):
        self.assertEqual(reverse_words("hello"), "hello")

    def test_empty_string(self):
        self.assertEqual(reverse_words(""), "")

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
