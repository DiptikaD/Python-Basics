from contextlib import contextmanager, redirect_stderr, redirect_stdout
from io import StringIO
from importlib.util import spec_from_file_location, module_from_spec
import os
from pathlib import Path
import shlex
import sys
from tempfile import NamedTemporaryFile
import unittest
import warnings


class GuessVPTests(unittest.TestCase):

    def test_always_incorrect_year(self):
        with patch_stdin("1600\n"):
            output = run_program("guess_vp.py")
        self.assertIn("That's not right.", output)
        self.assertNotIn("It could be!", output)

    def test_eventually_correct(self):
        for _ in range(1000):
            with patch_stdin("1979\n"):
                output = run_program("guess_vp.py")
                if "Walter Mondale" in output:
                    break
        self.assertIn("Walter Mondale", output)
        self.assertIn("It could be!", output)
        self.assertNotIn("That's not right.", output)
        self.assertIn("1977 to 1981", output, "Term should be shown")

    def test_eventually_incorrect(self):
        for _ in range(1000):
            with patch_stdin("1979\n"):
                output = run_program("guess_vp.py")
                if "Walter Mondale" not in output:
                    break
        self.assertNotIn("Walter Mondale", output)
        self.assertNotIn("It could be!", output)
        self.assertIn("That's not right.", output)
        self.assertNotIn("1977 to 1981", output, "Term should be shown")


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
def make_file(contents=None):
    """Context manager providing name of a file containing given contents."""
    with NamedTemporaryFile(mode='wt', encoding='utf-8', delete=False) as f:
        if contents:
            f.write(contents)
    try:
        yield f.name
    finally:
        os.remove(f.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
