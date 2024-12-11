from contextlib import contextmanager, redirect_stdout, redirect_stderr
from io import StringIO
from importlib.util import spec_from_file_location, module_from_spec
import os
from pathlib import Path
import shlex
import sys
from textwrap import dedent
from tempfile import NamedTemporaryFile
import unittest
import warnings


class UnsmartTests(unittest.TestCase):

    """Tests for unsmart.py."""

    def assert_expected_output(self, file_contents, expected_output):
        with make_file(file_contents) as filename:
            actual_output = run_program(f'unsmart.py {filename}')
        if actual_output.strip() == expected_output.strip():
            return  # Success!
        if actual_output.split() != expected_output.split():
            # More than a simple whitespace difference
            message = f"{actual_output!r} != {expected_output!r}\n\n"
            message += f"File contents:\n{file_contents}\n\n"
            message += f"Expected output:\n{expected_output}\n\n"
            message += f"Actual output:\n{actual_output}\n\n"
        else:
            # Just a whitespace difference
            message = dedent(f"""
                {actual_output!r} != {expected_output!r}\n
                File contents:    {file_contents!r}
                Expected output:  {expected_output!r}
                Actual output:    {actual_output!r}
            """).strip("\n")
        if actual_output == "":
            message += "\n\nDid you write a function and forget to call it?"
        raise self.failureException(message)

    def test_with_smart_quotes(self):
        self.assert_expected_output(
            '“This is a quotation”',
            '"This is a quotation"',
        )

    def test_with_smart_single_quotes(self):
        self.assert_expected_output(
            "This word is ‘quoted’.",
            "This word is 'quoted'.",
        )

    def test_with_smart_apostrophe(self):
        self.assert_expected_output(
            "Look, it’s an apostrophe!",
            "Look, it's an apostrophe!",
        )

    def test_multiple_lines(self):
        contents = dedent("""
            This text has a number of “smart quotes”.
            For example there’s a “quotation with ‘nested’ quotes”.

            There’s also a second paragraph.
            It has a bit of text in it.
            But its’ text isn’t very meaningful.
            ‘Tis just an example of text with smart quotes.
        """).lstrip()
        expected = dedent("""
            This text has a number of "smart quotes".
            For example there's a "quotation with 'nested' quotes".

            There's also a second paragraph.
            It has a bit of text in it.
            But its' text isn't very meaningful.
            'Tis just an example of text with smart quotes.
        """).lstrip()
        self.assert_expected_output(contents, expected)


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
    """Context manager providing name of a file containing given contents."""
    with NamedTemporaryFile(mode='wt', encoding='utf-8', delete=False) as f:
        if contents:
            f.write(contents)
    try:
        yield f.name
    finally:
        os.remove(f.name)


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""
    class resultclass(unittest.TextTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=AllowUnexpectedSuccessRunner)
