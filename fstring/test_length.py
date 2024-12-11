import ast
from contextlib import contextmanager, redirect_stdout, redirect_stderr
from io import StringIO
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
import shlex
import sys
import unittest
import warnings


class LengthTests(unittest.TestCase):

    """Tests for the Length program."""

    def test_emma(self):
        response = "Emma"
        with patch_stdin(f"{response}\n"):
            self.assertRun(
                response,
                "Hi Emma!\nYour name has 4 characters in it.",
            )

    def test_multiple_words(self):
        response = "Trey Hunner"
        with patch_stdin(f"{response}\n"):
            self.assertRun(
                response,
                "Hi Trey Hunner!\nYour name has 11 characters in it.",
            )

    # To test the bonus, comment out the next line
    @unittest.expectedFailure
    def test_interpolation_used(self):
        tree = ast.parse((DIRECTORY / "length.py").read_text())
        f_string_nodes = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.JoinedStr)
        ]
        replacement_fields = [
            node
            for f_string_node in f_string_nodes
            for node in f_string_node.values
            if isinstance(node, ast.FormattedValue)
        ]
        self.assertGreaterEqual(len(f_string_nodes), 1, "Expected f-string")
        self.assertGreaterEqual(
            len(replacement_fields),
            1,
            "Expected a {replacement} field",
        )

    def assertRun(self, response, expected):
        program = "length.py"
        prompt = "What's your name? "
        actual = run_program(f"{program}").strip()
        actual = actual.removeprefix(prompt)
        if actual == expected:
            return  # Success!
        message = f"{actual!r} != {expected!r}\n\n"
        message += f"Ran with input:\n{response}\n\n"
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


def run_program(
    arguments,
    raises=DummyException,
    stderr=False,
    allow_error=False,
):
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
                    if e.args not in [(0,), (None,)] and not allow_error:
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
    finally:
        sys.stdin = real_stdin


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
