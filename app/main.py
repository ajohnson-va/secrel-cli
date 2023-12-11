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
    ) # gh workflow run $WORKFLOW_FILE -R(epo) department-of-veterans-affairs/$TEST_REPO -r(ef) e2e-test-$REPO $INPUTS


if __name__ == '__main__':
    secrel()
