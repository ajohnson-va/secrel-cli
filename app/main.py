import click
import subprocess


@click.group()
def secrel():
    """SecRel CLI."""
    pass

@secrel.group()
def pipeline():
    """Pipeline operations."""
    pass

@pipeline.command()
@click.option(
    '-r', '--ref',
    default='main',
    required=False,
    help='The git ref or branch of the pipeline to run.'
)
def run(ref):
    """Run the pipeline."""
    subprocess.run(
        [
            'gh', 'workflow', 'run', 'pipeline.yml',
            '-R', 'department-of-veterans-affairs/lighthouse-tornado-secrel-pipeline',
            '-r', ref
        ],
        check=True
    )
    # TODO: better handling for non-zero code returns (failures)

@pipeline.command()
@click.option(
    '-r', '--ref',
    default='main',
    required=False,
    help='The git ref or branch of the pipeline E2E tests to run.'
)
def test(ref):
    """Test the pipeline."""
    subprocess.run(
        [
            'gh', 'workflow', 'run', 'e2e.yml',
            '-R', 'department-of-veterans-affairs/lighthouse-tornado-secrel-pipeline',
            '-r', ref
        ],
        check=True
    )


if __name__ == '__main__':
    secrel()
