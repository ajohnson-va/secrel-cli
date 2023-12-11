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
        ['gh', 'repo', 'view', 'department-of-veterans-affairs/lighthouse-tornado-secrel-pipeline'],
        check=True
    )

@pipeline.command()
def test():
    """Test the pipeline."""
    subprocess.run(
        ['gh', 'repo', 'view', 'department-of-veterans-affairs/lighthouse-tornado-secrel-pipeline'],
        check=True
    )


if __name__ == '__main__':
    secrel()
