from distutils.cmd import Command
from distutils.log import INFO
from distutils.errors import DistutilsError
from setuptools import setup
from subprocess import run, CalledProcessError


class TestCommand(Command):
    """A custom command to run lint, tests, and coverage."""

    description = "run lint, tests, and coverage on Python source files"
    user_options = [
        ("fail-fast", None, "Stop after first failed command."),
        ("no-lint", None, "Don't run linter (flake8)."),
        ("no-typecheck", None, "Don't run static typechecker (mypy)."),
        ("no-tests", None, "Don't run tests (pytest)."),
        ("no-coverage", None, "Don't generate coverage report."),
    ]

    def initialize_options(self):
        """Set default values for options."""
        self.fail_fast = False
        self.no_lint = False
        self.no_typecheck = False
        self.no_tests = False
        self.no_coverage = False

    def finalize_options(self):
        self.fail_fast = bool(self.fail_fast)
        self.no_lint = bool(self.no_lint)
        self.no_typecheck = bool(self.no_typecheck)
        self.no_tests = bool(self.no_tests)
        self.no_coverage = bool(self.no_coverage)

    def run(self):
        """Run command."""
        commands = []
        if not self.no_lint:
            commands.append(["flake8"])
        if not self.no_typecheck:
            commands.append(["mypy", "importit"])
        if not self.no_tests:
            commands.append(
                ["pytest"] if self.no_coverage else ["pytest", "--cov=importit"]
            )
        any_command_failed = False
        for command in commands:
            self.announce("running command: {}".format(" ".join(command)), level=INFO)
            try:
                run(command, check=True)
            except CalledProcessError:
                any_command_failed = True
                if self.fail_fast:
                    break

        if any_command_failed:
            raise DistutilsError("tests failed")


if __name__ == "__main__":
    setup(cmdclass={"test": TestCommand})
