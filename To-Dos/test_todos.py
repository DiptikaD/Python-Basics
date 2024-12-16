from contextlib import contextmanager, redirect_stdout, redirect_stderr
from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec
from io import StringIO
import shlex
import sys
from tempfile import NamedTemporaryFile
from textwrap import dedent
import unittest
import warnings


class TodosTests(unittest.TestCase):

    """Tests for todos.py."""

    def test_basic_functionality(self):
        contents = undent("""
            TODO starts with TODO
            This line has no to-do
            TODO another
        """)
        expected = undent("""
            TODO starts with TODO
            TODO another
        """)
        with make_file(contents) as filename:
            self.assertOutput(
                contents,
                run_program(f"todos.py {filename}").rstrip(),
                expected,
            )

    def test_todo_anywhere_in_line(self):
        contents = undent("""
            Ends with TODO
            This line has no to-do
            Has TODO in the middle of the line
            Just a regular line
            And another
            .. TODO in the middle again
            Last line
        """)
        expected = undent("""
            Ends with TODO
            Has TODO in the middle of the line
            .. TODO in the middle again
        """)
        with make_file(contents) as filename:
            self.assertOutput(
                contents,
                run_program(f"todos.py {filename}").rstrip(),
                expected,
            )

    def test_within_word(self):
        contents = undent("""
            Ends with TODO!
            This line has no to-do
            TODO: with a colon after
            Here's aTODOline
            And another
            Last line
        """)
        expected = undent("""
            Ends with TODO!
            TODO: with a colon after
            Here's aTODOline
        """)
        with make_file(contents) as filename:
            self.assertOutput(
                contents,
                run_program(f"todos.py {filename}").rstrip(),
                expected,
            )

    def test_no_todos(self):
        contents = "This file\nis done!\n"
        expected = ""
        with make_file(contents) as filename:
            self.assertOutput(
                contents,
                run_program(f"todos.py {filename}").rstrip(),
                expected,
            )

    def test_multiple_todos_per_line(self):
        contents = undent("""
            TODO: and TODO and TODO
            Another line
        """)
        expected = undent("""
            TODO: and TODO and TODO
        """)
        with make_file(contents) as filename:
            self.assertOutput(
                contents,
                run_program(f"todos.py {filename}").rstrip(),
                expected,
            )

    def assertOutput(self, contents, actual, expected):
        if actual == expected:
            return  # Success!
        message = f"{actual!r} != {expected!r}\n\n"
        message += f"File contents:\n{contents}\n\n"
        message += f"Expected output:\n{expected}\n\n"
        message += f"Actual output:\n{actual}"
        if actual == "":
            message += "\n\nDid you write a function and forget to call it?"
        raise self.failureException(message)


try:
    DIRECTORY = Path(__file__).resolve().parent
except NameError:
    DIRECTORY = Path.cwd()


class DummyException(Exception):
    """No code will ever raise this exception."""


def run_program(arguments, raises=DummyException, stderr=False):
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


def undent(text, rstrip=True):
    text = dedent(text).lstrip("\n")
    if rstrip:
        text = text.rstrip("\n")
    return text


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""
    class resultclass(unittest.TextTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=AllowUnexpectedSuccessRunner)
