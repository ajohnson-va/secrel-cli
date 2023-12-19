# SecRel CLI
Command line interface for Secure Release (SecRel) pipelines that enable continuous Risk Management Framework (cRMF) compliance.

## Installation

To install the SecRel CLI locally for use or development, follow these steps:

### Clone the repository

Using the GitHub CLI:

```bash
gh repo clone ajohnson-va/secrel-cli
```

Using Git:

```bash
git clone ajohnson-va/secrel-cli
```

### Install the app

From the root of the cloned repository, run the install script:

```bash
./scripts/install-app.sh
```

_Note that the install script is idempotent, so it can be used to reinstall the CLI if needed during local development and testing._

For local development, it's best to install the app in a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
./scripts/install-app.sh
```

## Configuration

In order to use the SecRel CLI, you can either setup a configuration file named `.secrelrc` in your home directory:

`~/.secrel`

```ini
[ORGANIZATION]
NAME = some-organization

[PIPELINE]
REPO = secrel-demo-pipeline
WORKFLOW = pipeline.yaml
E2E_TESTS = e2e.yaml
DEFAULT_BRANCH = main
```

Or, export the following environment variables:

```bash
export ORGANIZATION='some-organization'
export PIPELINE_REPO='secrel-demo-pipeline'
export PIPELINE_WORKFLOW='pipeline.yaml'
export PIPELINE_E2E_TESTS='e2e.yaml'
export PIPELINE_DEFAULT_BRANCH='main'
```

## Usage

To use the SecRel CLI, run the `secrel` command:

```bash
secrel
```

This will display the help text and commands available for use.
