from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec
from io import StringIO
import shlex
import sys
import unittest
import warnings


class RollTests(unittest.TestCase):

    """Tests for roll.py."""

    def test_no_arguments(self):
        for _ in range(60):
            self.assertIn(
                run_program("roll.py").strip(),
                {str(n) for n in range(1, 7)},
                "Output should always be 1, 2, 3, 4, 5, or 6",
            )

    def test_all_options_possible(self):
        outputs_after_60_rolls = {
            run_program("roll.py").strip()
            for _ in range(60)
        }
        self.assertEqual(
            outputs_after_60_rolls,
            {"1", "2", "3", "4", "5", "6"},
            "Rolling 60 times should produce all possible values",
        )


# To test bonus 1, comment out the next line
@unittest.expectedFailure
class RollWithArgumentTests(unittest.TestCase):

    def test_invalid_argument(self):
        with self.assertRaises(BaseException):
            run_program("roll.py 4.5")

    def test_one_large_argument(self):
        roll1 = run_program("roll.py 20")
        roll2 = run_program("roll.py 20")
        roll3 = run_program("roll.py 20")
        roll4 = run_program("roll.py 20")
        roll5 = run_program("roll.py 20")
        rolls = [roll1, roll2, roll3, roll4, roll5]
        possibilities = {f"{n}\n" for n in range(1, 21)}
        for roll in rolls:
            self.assertIn(roll, possibilities)
        self.assertGreater(len(set(rolls)), 1)

    def test_3_sided_die_possibilities(self):
        outputs_after_30_rolls = {
            run_program("roll.py 3").strip()
            for _ in range(30)
        }
        self.assertEqual(
            outputs_after_30_rolls,
            {"1", "2", "3"},
            "Rolling 3-sided die 30 times should eventually show 1, 2, and 3",
        )


# To test bonus 2, comment out the next line
@unittest.expectedFailure
class RollWithMultipleArgumentsTests(unittest.TestCase):

    def test_many_arguments(self):
        rolls = [
            run_program("roll.py 6 6 6 6")
            for _ in range(15)
        ]
        possibilities = {f"{n}\n" for n in range(4, 25)}
        for roll in rolls:
            self.assertIn(roll, possibilities)
        self.assertLess(len(set(rolls)), len(rolls))
        self.assertGreater(len(set(rolls)), 3)

    def test_2_3_sided_die_possibilities(self):
        outputs_after_30_rolls = {
            run_program("roll.py 3 3").strip()
            for _ in range(60)
        }
        self.assertEqual(
            outputs_after_30_rolls,
            {"2", "3", "4", "5", "6"},
            "Rolling 2 3-sided die 60 times should produce 2 through 6",
        )


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


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""
    class resultclass(unittest.TextTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    from platform import python_version
    if sys.version_info < (3, 6):
        sys.exit("Running {}.  Python 3.6 required.".format(python_version()))
    unittest.main(verbosity=2, testRunner=AllowUnexpectedSuccessRunner)
