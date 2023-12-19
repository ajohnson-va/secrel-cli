from click.testing import CliRunner

from app.main import secrel


def test_run_command():
    runner = CliRunner()
    result = runner.invoke(secrel, ['pipeline', 'run'])

    assert result.exit_code == 0

def test_test_command():
    runner = CliRunner()
    result = runner.invoke(secrel, ['pipeline', 'test'])

    assert result.exit_code == 0
