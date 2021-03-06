#! /usr/bin/env python3

from setuptools import setup
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='msiempy',
    description="McAfee SIEM API Python wrapper",
    url='https://github.com/mfesiem/msiempy',
    maintainer='andywalden, tristanlatr',
    maintainer_email='aw@krakencodes.com, tris.la.tr@gmail.com',
    version='0.0.1',
    packages=['msiempy',],
    entry_points = {
        'console_scripts': ['msiempy=msiempy.cli:main'],
    },
    install_requires=[
          'requests','tqdm','PTable','python-dateutil'
    ],
    tests_require=[
          'pylint','pytest'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    license='The MIT License',
    long_description=README,
    long_description_content_type="text/markdown",
    test_suite="tests"
)