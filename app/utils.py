import subprocess
import sys
import os
import configparser


def handle_error(error, missing_keys=None,
                 workflow=None, org=None, repo=None, ref=None):

    if error == "missing_config_keys":
        print(
            "❌ ERROR: Missing value for configuration setting(s):\n\n" +
            '\n'.join(missing_keys) + "\n\n"
            "Please define in ~/.secrelrc "
            "or set as environment variable(s) and try again."
        )
        sys.exit(1)

    error_msg = error.stderr.strip()
    if "Workflow does not have 'workflow_dispatch' trigger" in error_msg:
        print(
            "❌ ERROR: no workflow_dispatch:' to\n"
            f"{workflow} on braworkflow_dispatch trigger found.\n"
            f"workflow file: {workflow}\n"
            f"pipeline: {org}/{repo}\n"
            f"branch: {ref}\n\n"
            "Correct by specifying a different branch "
            "for the run using '-r' or '--ref':\n\n  "
            "secrel pipeline run -r your-branch\n\n"
            "or, by adding 'on.nch {ref} of the repo and try again."
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

    return config

def load_config():
    config = read_config()
    config_dict = {
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

    missing_keys = [
        key for key, value in config_dict.items() if value is None
    ]

    if missing_keys:
        handle_error("missing_config_keys", missing_keys)

    return config_dict


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
            error=e,
            workflow=workflow,
            org=org,
            repo=repo,
            ref=ref
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
