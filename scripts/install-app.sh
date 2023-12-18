#!/bin/bash

# Check if secrel-cli is installed
if pip show secrel-cli &> /dev/null; then
    echo "secrel-cli is already installed; uninstalling..."
    pip uninstall -y secrel-cli
else
    echo "secrel-cli is not installed."
fi

# Install secrel-cli
echo "Installing secrel-cli..."
pip install .
