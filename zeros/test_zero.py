from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
import shlex
import shutil
import sys
import unittest
import warnings


class ZeroTests(unittest.TestCase):

    """Tests for zero.py."""

    def test_output(self):
        self.assertRun(
            "",
            "0000000000000000000000000000000000000000" +
            "0000000000000000000000000000000000000000\n",
        )

    # To test bonus 1, comment out the next line
    @unittest.expectedFailure
    def test_accepts_number(self):
        self.assertRun("5", "00000\n")
        self.assertRun(
            "90",
            "000000000000000000000000000000000000000000000" +
            "000000000000000000000000000000000000000000000\n",
        )
        self.assertRun(
            "120",
            "000000000000000000000000000000000000000000000000000000000000" +
            "000000000000000000000000000000000000000000000000000000000000\n",
        )

    # To test bonus 2, comment out the next line
    @unittest.expectedFailure
    def test_accepts_multiple_number(self):
        self.assertRun("2 4 6", "00\n0000\n000000\n")
        self.assertRun(
            "80 90",
            "0000000000000000000000000000000000000000" +
            "0000000000000000000000000000000000000000\n" +
            "000000000000000000000000000000000000000000000" +
            "000000000000000000000000000000000000000000000\n",
        )
        self.assertRun(
            "79 80 90 120",
            "0000000000000000000000000000000000000000" +
            "000000000000000000000000000000000000000\n" +
            "0000000000000000000000000000000000000000" +
            "0000000000000000000000000000000000000000\n" +
            "000000000000000000000000000000000000000000000" +
            "000000000000000000000000000000000000000000000\n" +
            "000000000000000000000000000000000000000000000000000000000000" +
            "000000000000000000000000000000000000000000000000000000000000\n",
        )

    def assertRun(self, arguments, expected):
        program = "zero.py"
        command = f"{program} {arguments}"
        actual = run_program(command)
        if actual.strip() == expected.strip():
            return  # Success!
        message = f"{actual!r} != {expected!r}\n\n"
        message += f"Ran:\n{executable()} {command}\n\n"
        message += f"Expected output:\n{expected}\n"
        message += f"Actual output:\n{actual.rstrip()}"
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


def executable():
    """Return simplest "python" command that seems to work."""
    possible_executables = [
        "python", "python3",
        *(f"python3.{n}" for n in range(14, 8, -1)),
    ]
    for name in possible_executables:
        if shutil.which(name) == sys.executable:
            return name
    if shutil.which("py"):
        return "py"
    return sys.executable


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""
    class resultclass(unittest.TextTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=AllowUnexpectedSuccessRunner)
