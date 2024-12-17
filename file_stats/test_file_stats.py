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


class FileStatsTests(unittest.TestCase):

    """Tests for file_stats.py"""

    def test_basic_functionality(self):
        contents = undent("""
            This is a file.
            With two lines in it.
        """)
        with make_file(contents) as filename:
            output = run_program(f"file_stats.py {filename}")
            self.assertOutput(contents, output, "Lines: 2\nWords: 9\n")

    def test_single_line_file(self):
        contents = "This is a single line file."
        with make_file(contents) as filename:
            output = run_program(f"file_stats.py {filename}")
            self.assertOutput(contents, output, "Lines: 1\nWords: 6\n")

    def test_single_word(self):
        contents = "Hello"
        with make_file(contents) as filename:
            output = run_program(f"file_stats.py {filename}")
            self.assertOutput(contents, output, "Lines: 1\nWords: 1\n")

    def test_file_ending_with_newline(self):
        contents = "This file ends with a newline\n"
        with make_file(contents) as filename:
            output = run_program(f"file_stats.py {filename}")
            self.assertOutput(contents, output, "Lines: 1\nWords: 6\n")

    def test_file_with_multiple_empty_lines(self):
        contents = undent("""
            Line one


            Line four
        """)
        with make_file(contents) as filename:
            output = run_program(f"file_stats.py {filename}")
            self.assertOutput(contents, output, "Lines: 4\nWords: 4\n")

    def assertOutput(self, contents, actual, expected):
        if actual == expected:
            return  # Success!
        message = dedent(f"""
            {actual!r} != {expected!r}\n
            File contents:    {contents!r}
            Expected output:  {expected!r}
            Actual output:    {actual!r}
        """).strip("\n")
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
                    sys.modules["__main__"] = None  # Closes any open files

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


if __name__ == "__main__":
    unittest.main(verbosity=2)
