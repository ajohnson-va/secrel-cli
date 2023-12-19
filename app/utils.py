import subprocess
import sys
import os
import configparser


def handle_error(error, workflow, org, repo, ref):
    error_msg = error.stderr.strip()
    if "Workflow does not have 'workflow_dispatch' trigger" in error_msg:
        print(
            "❌ ERROR: workflow_dispatch trigger not found in workflow file.\n"
            f"workflow file: {workflow}\n"
            f"pipeline: {org}/{repo}\n"
            f"branch: {ref}\n\n"
            "Correct by specifying a different branch "
            "using '-r' or '--ref':\n\n  "
            "secrel pipeline run -r your-branch\n\n"
            "or, by adding 'workflow_dispatch:'\n"
            f"to the 'on:' section of {workflow}\n"
            f"on the branch {ref} and try again."
        )
        sys.exit(1)
    print(
        "❌ ERROR: an unhandled exception occurred.\n"
        f"workflow file: {workflow}\n"
        f"pipeline: {org}/{repo}\n"
        f"branch: {ref}\n\n"
        f"The error was: {error_msg}"
    )
    sys.exit(1)

def read_config():
    config = configparser.ConfigParser()
    home_dir = os.path.expanduser("~")
    config_file = os.path.join(home_dir, '.secrelrc')
    if os.path.exists(config_file):
        config.read(config_file)
        return config
    print(f"No .secrelrc file found in {home_dir}")
    return config

def load_config():
    config = read_config()
    return {
        'ORGANIZATION': config.get(
            'ORGANIZATION', 'NAME',
            fallback=os.getenv('ORGANIZATION')
        ),
        'PIPELINE_REPO': config.get(
            'PIPELINE', 'REPO',
            fallback=os.getenv('PIPELINE_REPO')
        ),
        'PIPELINE_WORKFLOW': config.get(
            'PIPELINE', 'WORKFLOW',
            fallback=os.getenv('PIPELINE_WORKFLOW')
        ),
        'PIPELINE_E2E_TESTS': config.get(
            'PIPELINE', 'E2E_TESTS',
            fallback=os.getenv('PIPELINE_E2E_TESTS')
        ),
        'PIPELINE_DEFAULT_BRANCH': config.get(
            'PIPELINE', 'DEFAULT_BRANCH',
            fallback=os.getenv('PIPELINE_DEFAULT_BRANCH')
        ),
    }

def run_workflow(workflow, org, repo, ref):
    try:
        subprocess.run(
            [
                'gh', 'workflow', 'run', f'{workflow}',
                '-R', f'{org}/{repo}',
                '-r', ref
            ],
            check=True,
            stderr=subprocess.PIPE,
            text=True
        )
    except subprocess.CalledProcessError as e:
        handle_error(
            e, workflow, org, repo, ref
        )

def cancel_workflow(run_id):
    try:
        subprocess.run(
            [
                'gh', 'run', 'cancel', f'{run_id}'
            ],
            check=True,
            stderr=subprocess.PIPE,
            text=True
        )
    except subprocess.CalledProcessError as e:
        handle_error(
            e, "Unknown", "Unknown", "Unknown", "Unknown"
        )
