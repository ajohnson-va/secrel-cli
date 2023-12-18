import subprocess
import sys


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
