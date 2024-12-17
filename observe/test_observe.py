import ast
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from io import StringIO
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
import shlex
import sys
from textwrap import dedent
import unittest
from unittest.mock import Mock, patch
import warnings


class ObserveTests(unittest.TestCase):
    def setUp(self):
        """Monkey-patch time module and prep sys.stdout.write for patching."""

        self.clock = Clock()

        self.sleep_patch = patch(
            "time.sleep",
            side_effect=self.clock.increment,
        )
        self.sleep_mock = self.sleep_patch.start()

        self.mocks = Mock()
        self.mocks.attach_mock(self.sleep_mock, "sleep")

    def tearDown(self):
        """Undo all our monkey-patching."""
        self.sleep_patch.stop()
        self.clock.reset()

    def reset_mocks(self):
        self.mocks.reset_mock()
        self.mocks.stdout_write.reset_mock()
        self.mocks.stderr_write.reset_mock()
        self.clock.reset()

    @contextmanager
    def patch_print(self):
        print_patch = patch("builtins.print")
        self.mocks.attach_mock(print_patch.start(), "print")
        try:
            yield self.mocks.print
        finally:
            print_patch.stop()

    def test_printed_output(self):
        clear = "\r\033[K"
        self.assertRun(
            f"Listen...{clear}" +
            f"Look...{clear}" +
            f"Smell...{clear}" +
            f"Sit...{clear}" +
            "Done\n"
        )

    def test_sleep_for_1_second_each(self):
        with self.patch_print():
            run_program("observe.py")
        self.assertEqual(
            [call.args[0] for call in self.mocks.sleep.mock_calls],
            [1] * 16,
            "sleep exactly 16 times for 1 second each",
        )

    def test_sleep_between_printing(self):
        with self.patch_print():
            run_program("observe.py")
        self.assertEqual(
            [call[0] for call in self.mocks.mock_calls][:36],
            ["print", *("sleep", "print")*4] * 4,
            "Must printing and sleep in a precise order",
        )

    def test_loop_used(self):
        tree = ast.parse((DIRECTORY / "observe.py").read_text())
        loop_nodes = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.For)
        ]
        prints_in_loops = [
            node
            for loop_node in loop_nodes
            for node in ast.walk(loop_node)
            if isinstance(node, ast.Call) and node.func.id == "print"
        ]
        self.assertGreaterEqual(
            len(loop_nodes),
            1,
            "Expected at least one loop",
        )
        self.assertGreaterEqual(
            len(prints_in_loops),
            1,
            "Expected at least one print in a loop",
        )

    def assertRun(self, expected):
        actual = run_program("observe.py")
        if actual == expected:
            return  # Success!
        message = dedent(f"""
            {actual!r} != {expected!r}\n
            Expected output:    {expected!r}
            Actual output:      {actual!r}
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
                    sys.modules.pop("__main__", None)  # Closes any open files

                if stderr:
                    return output.getvalue(), error.getvalue()
                else:
                    return output.getvalue()
    finally:
        sys.argv = old_args  # Undo the monkey patching of sys.argv


class Clock:

    """Fake version of time.perf_counter."""

    def __init__(self):
        self.sleeps = []

    def __call__(self):
        return sum(self.sleeps)

    def reset(self):
        self.sleeps.clear()

    def increment(self, count):
        self.sleeps.append(count)


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""
    class resultclass(unittest.TextTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=AllowUnexpectedSuccessRunner)
