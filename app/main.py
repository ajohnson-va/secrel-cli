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
def run():
    """Run the pipeline."""
    subprocess.run(
        [
            'gh', 'workflow', 'run', 'pipeline.yml',
            '-R', 'department-of-veterans-affairs/lighthouse-tornado-secrel-pipeline',
            '-r', 'tony-test-branch'
        ],
        check=True
    )

@pipeline.command()
def test():
    """Test the pipeline."""
    subprocess.run(
        [
            'gh', 'workflow', 'run', 'e2e.yml',
            '-R', 'department-of-veterans-affairs/lighthouse-tornado-secrel-pipeline',
            '-r', 'tony-test-branch'
        ],
        check=True
    )


if __name__ == '__main__':
    secrel()
