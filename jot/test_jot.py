from contextlib import contextmanager, redirect_stderr, redirect_stdout
from io import StringIO
from importlib.util import spec_from_file_location, module_from_spec
import os
from pathlib import Path
import shlex
import sys
from tempfile import TemporaryDirectory
from textwrap import dedent
import unittest
import warnings


class JotTests(unittest.TestCase):

    """Tests for jot.py."""

    home_keys = ['HOMEPATH', 'HOME', 'USERPROFILE', 'HOMEDRIVE', 'USERNAME']

    def setUp(self):
        """Patch current date and home directory."""
        self.patched_date = patch_date(2024, 10, 2, 10, 30)
        self.set_date = self.patched_date.__enter__()

        self.environ = {
            name: os.environ[name]
            for name in self.home_keys
            if name in os.environ
        }
        for key in self.home_keys:
            os.environ.pop(key, None)
        self.home = TemporaryDirectory()
        os.environ['HOMEPATH'] = os.environ['HOME'] = self.home.name

    def tearDown(self):
        """Unpatch current date and home directory."""
        self.patched_date.__exit__(None, None, None)
        os.environ.update(self.environ)
        self.home.cleanup()

    def test_single_jot_written(self):
        with patch_stdin("First jot!\n"):
            run_program("jot.py")
        jot_path = Path(self.home.name, "jot.txt")
        contents = jot_path.read_text()
        self.assertEqual(contents, "2024-10-02 First jot!\n")

    def test_two_jots_same_day(self):
        with patch_stdin("First jot!\n"):
            run_program("jot.py")
        with patch_stdin("Second jot, same day\n"):
            run_program("jot.py")
        jot_path = Path(self.home.name, "jot.txt")
        contents = jot_path.read_text()
        self.assertEqual(contents, dedent("""
            2024-10-02 First jot!
            2024-10-02 Second jot, same day
        """).lstrip("\n"))


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
def patch_stdin(text):
    real_stdin = sys.stdin
    sys.stdin = StringIO(text)
    try:
        yield sys.stdin
    except EOFError as e:
        raise AssertionError("Kept prompting for input too long") from e
    finally:
        sys.stdin = real_stdin


@contextmanager
def patch_date(year, month, day, hour=0, minute=0):
    """Monkey patch the current time to be the given time."""
    import datetime
    from unittest.mock import patch

    date_args = year, month, day
    time_args = hour, minute

    class FakeDate(datetime.date):
        """A datetime.date class with mocked today method."""

        @classmethod
        def today(cls):
            return cls(*date_args)

    class FakeDateTime(datetime.datetime):
        """A datetime.datetime class with mocked today, now methods."""

        @classmethod
        def today(cls):
            return cls(*date_args, *time_args)

        @classmethod
        def now(cls):
            return cls.today()

    def set_date(year, month, day, *rest):
        nonlocal date_args, time_args
        date_args = year, month, day
        time_args = rest

    FakeDate.__name__ = 'date'
    FakeDateTime.__name__ = 'datetime'
    with patch('datetime.datetime', FakeDateTime):
        with patch('datetime.date', FakeDate):
            yield set_date


if __name__ == "__main__":
    from platform import python_version
    if sys.version_info < (3, 6):
        sys.exit("Running {}.  Python 3.6 required.".format(python_version()))
    unittest.main(verbosity=2)
