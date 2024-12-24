import ast
import inspect
from textwrap import dedent
import unittest
from flip_dict import flip_dict


class FlipDictTests(unittest.TestCase):

    """Tests for flip_dict."""

    def test_empty_dict(self):
        self.assertEqual(flip_dict({}), {})

    def test_one_item_dict(self):
        self.assertEqual(flip_dict({'a': 1}), {1: 'a'})

    def test_no_collisions(self):
        inputs = {
            'Python': "2015-09-15",
            'Java': "2015-09-14",
            'C': "2015-09-13",
        }
        outputs = {
            '2015-09-13': 'C',
            '2015-09-15': 'Python',
            '2015-09-14': 'Java',
        }
        self.assertEqual(flip_dict(inputs), outputs)

    def test_with_collisions(self):
        inputs = {
            'Python': "2015-09-15",
            'Java': "2015-09-14",
            'C': "2015-09-13",
            'JavaScript': "2015-09-13",
        }
        outputs = {
            '2015-09-13': 'JavaScript',
            '2015-09-15': 'Python',
            '2015-09-14': 'Java',
        }
        self.assertEqual(flip_dict(inputs), outputs)

    def test_original_dictionary_unchanged(self):
        inputs = {
            'Python': "2015-09-15",
            'Java': "2015-09-14",
            'C': "2015-09-13",
            'JavaScript': "2015-09-13",
        }
        flip_dict(inputs)
        self.assertEqual(inputs, {
            'Python': "2015-09-15",
            'Java': "2015-09-14",
            'C': "2015-09-13",
            'JavaScript': "2015-09-13",
        }, "The given dictionary should not change")

    # To test bonus 1, comment out the next line
    @unittest.expectedFailure
    def test_with_error_on_duplicates(self):
        no_dups = {
            'Python': "2015-09-15",
            'Java': "2015-09-14",
            'C': "2015-09-13",
        }
        outputs = {
            '2015-09-13': 'C',
            '2015-09-15': 'Python',
            '2015-09-14': 'Java',
        }
        self.assertEqual(flip_dict(no_dups, error_on_duplicates=True), outputs)

        has_dups = {
            'Python': "2015-09-15",
            'Java': "2015-09-14",
            'C': "2015-09-13",
            'JavaScript': "2015-09-13",
        }
        with self.assertRaises(ValueError):
            flip_dict(has_dups, error_on_duplicates=True)

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


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""
    class resultclass(unittest.TextTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=AllowUnexpectedSuccessRunner)
