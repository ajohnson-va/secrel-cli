import os

from click.testing import CliRunner

from app.main import secrel


TEST_BRANCH = os.getenv("TEST_BRANCH")


def test_run_command():
    runner = CliRunner()
    result = runner.invoke(secrel, ['pipeline', 'run', '-r', TEST_BRANCH])
    print(result)
    print(result.exit_code)
    print(result.exc_info)
    print(result.output)
    print(result.exception)

    assert result.exit_code == 0

def test_test_command():
    runner = CliRunner()
    result = runner.invoke(secrel, ['pipeline', 'test', '-r', TEST_BRANCH])
    print(result)
    print(result.exit_code)
    print(result.exc_info)
    print(result.output)
    print(result.exception)

    assert result.exit_code == 0
