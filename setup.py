from setuptools import find_packages, setup


setup(
    name='secrel_cli',
    packages=find_packages(include=['app']),
    version='0.1.0',
    description='Command line interface for SecRel components',
    author='Anthony T. Johnson',
    install_requires=['click'],
    python_requires='>=3.11',
    # test_suite='tests',
    entry_points={
        'console_scripts': [
            'secrel = app.main:secrel',
        ],
    },
)
