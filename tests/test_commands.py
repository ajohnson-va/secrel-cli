import os

from click.testing import CliRunner

from app.main import secrel


TEST_BRANCH = os.getenv("TEST_BRANCH")


def test_run_command():
    runner = CliRunner()
    result = runner.invoke(secrel, ['pipeline', 'run', '-r', TEST_BRANCH])

    assert result.exit_code == 0

def test_test_command():
    runner = CliRunner()
    result = runner.invoke(secrel, ['pipeline', 'test', '-r', TEST_BRANCH])

    assert result.exit_code == 0
