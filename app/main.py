import click

from . import utils

# TODO: tests in CI need appropriate GH token
# TODO: README.md
# TODO: cancel runs, especially test ones
# TODO: gh issue
# TODO: gh run list

ORGANIZATION = 'department-of-veterans-affairs'
PIPELINE_REPO = 'lighthouse-tornado-secrel-pipeline'
PIPELINE_WORKFLOW = 'pipeline.yml'
PIPELINE_E2E_TESTS = 'e2e.yml'
PIPELINE_DEFAULT_BRANCH = 'main'


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
    default=PIPELINE_DEFAULT_BRANCH,
    required=False,
    help='The git ref or branch of the pipeline to run.'
)
def run(ref):
    """Run the pipeline."""
    utils.run_workflow(PIPELINE_WORKFLOW, ORGANIZATION, PIPELINE_REPO, ref)

@pipeline.command()
@click.option(
    '-r', '--ref',
    default=PIPELINE_DEFAULT_BRANCH,
    required=False,
    help='The git ref or branch of the pipeline E2E tests to run.'
)
def test(ref):
    """Test the pipeline."""
    utils.run_workflow(PIPELINE_E2E_TESTS, ORGANIZATION, PIPELINE_REPO, ref)


if __name__ == '__main__':
    secrel()
