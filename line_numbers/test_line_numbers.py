from contextlib import contextmanager, redirect_stdout, redirect_stderr
from pathlib import Path
from tempfile import NamedTemporaryFile
from importlib.util import spec_from_file_location, module_from_spec
from io import StringIO
import shlex
import sys
from textwrap import dedent
import unittest
import warnings


class LineNumbersTests(unittest.TestCase):

    """
    Tests for line_numbers.py.

    Output each line with its line number in front of it
    """

    maxDiff = 1000

    def assertOutput(self, contents, actual, expected):
        actual, expected = actual.rstrip(), expected.rstrip()
        if actual == expected:
            return  # Success!
        message = f"{actual!r} != {expected!r}\n\n"
        message += f"File contents:\n{contents}\n\n"
        message += f"Expected output:\n{expected}\n\n"
        message += f"Actual output:\n{actual}"
        if actual == "":
            message += "\n\nDid you write a function and forget to call it?"
        raise self.failureException(message)

    def test_lines(self):
        contents = dedent("""
            Oh what a day
            What a lovely day
        """.lstrip("\n"))
        expected = dedent("""
            1 Oh what a day
            2 What a lovely day
        """.lstrip("\n"))
        with make_file(contents) as filename:
            output = run_program(f"line_numbers.py {filename}")
        self.assertOutput(contents, output, expected)

    def test_more_lines(self):
        contents = dedent("""
            This file
            is two lines long.
            No wait, it's three lines long!
        """.lstrip("\n"))
        expected = dedent("""
            1 This file
            2 is two lines long.
            3 No wait, it's three lines long!
        """.lstrip("\n"))
        with make_file(contents) as filename:
            output = run_program(f"line_numbers.py {filename}")
        self.assertOutput(contents, output, expected)


try:
    DIRECTORY = Path(__file__).resolve().parent
except NameError:
    DIRECTORY = Path.cwd()


class DummyException(Exception):
    """No code will ever raise this exception."""


def run_program(arguments, *, raises=DummyException, stderr=False):
    """
    Run program at given path with given arguments.

    If raises is specified, ensure the given exception is raised.

    If stderr is True, separate stdout and stderr streams.
    """
    arguments = arguments.replace("\\", "\\\\")  # shlex posix=True workaround
    [path, *args] = shlex.split(arguments)
    path = str(DIRECTORY / path)
    old_args = sys.argv
    warnings.filterwarnings("ignore", r"unclosed file", ResourceWarning)
    try:
        sys.argv = [path, *args]  # Monkey-patch sys.argv
        with redirect_stdout(StringIO()) as output:
            error = StringIO() if stderr else output
            with redirect_stderr(error):
                try:
                    sys.modules.pop("__main__", None)
                    spec = spec_from_file_location("__main__", path)
                    module = module_from_spec(spec)
                    sys.modules["__main__"] = module
                    spec.loader.exec_module(module)
                # A specific exception should have been raised
                except raises as e:
                    # If sys.exit is called with a string, print it out
                    if isinstance(e, SystemExit):
                        if e.args and not isinstance(e.args[0], int):
                            if len(e.args) == 1:
                                error.write(str(e.args[0]))
                            else:
                                error.write(str(e.args))
                # An unexpected SystemExit exception was raised
                except SystemExit as e:
                    if e.args not in [(0,), (None,)]:
                        raise SystemExit(error.getvalue()) from e
                # No exception was raised
                else:
                    if raises is not DummyException:
                        raise AssertionError("{} not raised".format(raises))
                # Always force delete objects
                finally:
                    sys.modules["__main__"].__dict__.clear()
                    sys.modules.pop("__main__", None)  # Closes any open files

                if stderr:
                    return output.getvalue(), error.getvalue()
                else:
                    return output.getvalue()
    finally:
        sys.argv = old_args  # Undo the monkey patching of sys.argv


@contextmanager
def make_file(contents=None):
    with NamedTemporaryFile(mode='wt', delete=False) as f:
        if contents:
            f.write(contents)
    try:
        yield f.name
    finally:
        Path(f.name).unlink()


if __name__ == "__main__":
    from platform import python_version
    if sys.version_info < (3, 6):
        sys.exit("Running {}.  Python 3.6 required.".format(python_version()))
    unittest.main(verbosity=2)
