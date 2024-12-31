import ast
from collections import defaultdict, OrderedDict
import inspect
from pathlib import Path
from pprint import pformat
from textwrap import dedent
import unittest

from flip import flip_dict_of_lists


class FlipDictOfListsTest(unittest.TestCase):

    """Test for flip_dict_of_lists."""

    def test_flip_dict_of_lists(self):
        restaurants_by_people = {
            'Diane': ['Punjabi Tandoor', 'Opera'],
            'Peter': ['Opera', 'Habaneros'],
            'Trey': ['Habaneros', 'Opera', 'Punjabi Tandoor'],
        }
        favorite_restaurants = flip_dict_of_lists(restaurants_by_people)
        favorite_restaurants = {
            k: sorted(v)
            for k, v in favorite_restaurants.items()
        }
        self.assertEqual(favorite_restaurants, {
            'Opera': ['Diane', 'Peter', 'Trey'],
            'Habaneros': ['Peter', 'Trey'],
            'Punjabi Tandoor': ['Diane', 'Trey'],
        })

    def test_works_with_other_dict_types(self):
        dictionary = defaultdict(list)
        dictionary[1].append('a')
        dictionary[2] += ['a', 'b']
        dictionary[3] = ['b', 'c']
        flipped = flip_dict_of_lists(dictionary)
        self.assertEqual(flipped, {
            'a': [1, 2],
            'b': [2, 3],
            'c': [3],
        })

    def test_original_key_order_ordered_maintained(self):
        dictionary = OrderedDict([
            (1, ['a']),
            (2, ['a', 'b']),
            (3, ['b', 'c']),
        ])
        flipped = flip_dict_of_lists(dictionary)
        self.assertEqual(flipped, {
            'a': [1, 2],
            'b': [2, 3],
            'c': [3],
        })

    # To test bonus 1, comment out the next line
    @unittest.expectedFailure
    def test_custom_dict_type(self):
        dictionary = {'a': [1, 2], 'b': [2, 3]}
        dict_type = OrderedDict
        flipped = flip_dict_of_lists(dictionary, dict_type=dict_type)
        self.assertEqual(flipped, {
            1: ['a'],
            2: ['a', 'b'],
            3: ['b'],
        })
        self.assertEqual(type(flipped), dict_type)

    # To test bonus 2, comment out the next line
    @unittest.expectedFailure
    def test_key_function(self):
        dictionary = {
            1: ['a'],
            2: ['A', 'b'],
            3: ['B'],
        }
        def normalize(string): return string.upper()
        flipped = flip_dict_of_lists(dictionary, key_func=normalize)
        self.assertEqual(flipped, {
            'A': [1, 2],
            'B': [2, 3],
        })

    def assertEqual(self, actual, expected):
        if actual == expected:
            return  # Success!
        function_call = get_actual_function_call(inspect.currentframe().f_back)
        message = dedent(f"""
            {actual!r} != {expected!r}\n
            Ran:
            {function_call}
        """).strip("\n")
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
