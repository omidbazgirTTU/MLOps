"""
Test goes here

"""

from mylib.calculator import add
from click.testing import CliRunner
from main import add_cli


def test_add():
    assert add(1, 2) == 3


def test_help():
    """Tests the command-line interface help message."""
    runner = CliRunner()
    result = runner.invoke(add_cli, ["--help"])
    assert result.exit_code == 0
    assert "Show this message and exit." in result.output


# write a test for the add_cli function that calls the add_cli function with the arguments 1 and 2 and checks that the output is 3.
def test_add_cli():
    runner = CliRunner()

    # Test case 1: Check if the result is correct
    result = runner.invoke(add_cli, ["1", "2"])
    assert result.exit_code == 0  # Check if the command ran successfully
    # Check if the output contains the expected result
    assert "3" in result.output
