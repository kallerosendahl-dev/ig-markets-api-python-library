#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path
import io

NAME = "trading_ig"
filename = "%s/version.py" % NAME
with open(filename) as f:
    exec(f.read())

here = path.abspath(path.dirname(__file__))


def readme():
    filename = path.join(here, "README.rst")
    with io.open(filename, "rt", encoding="UTF-8") as f:
        return f.read()


setup(
    name=NAME,
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/development.html#single-sourcing-the-version
    # version='0.0.1',
    version= "0.0.9",
    description="A lightweight wrapper for the IG Markets API written in Python",
    long_description=readme(),
    # The project's main homepage.
    url="https://github.com/ig-python/ig-markets-api-python-library",
    # Author details
    author="Femto Trader",
    author_email="femto.trader@gmail.com",
    # Choose your license
    license="BSD",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Environment :: Console",
        # 'Topic :: Software Development :: Build Tools',
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Cython",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: BSD License",
    ],
    python_requires='>=3.6',
    # What does your project relate to?
    keywords="trading, spread betting, CFDs",
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/technical.html#install-requires-vs-requirements-files
    install_requires=[
        "munch==2.5.0",
        "pycryptodome==3.9.8",
        "requests==2.24.0",
        "requests-cache==0.5.2",
        "six==1.15.0",
        "pandas==1.2.0; python_version>='3.7.1'",
        "pandas==1.1.5; python_version<'3.7.1'"
    ],  # bunch->lunch->infi.bunch->munch
    # List additional groups of dependencies here (e.g. development dependencies).
    # You can install these using the following syntax, for example:
    # $ pip install -e .[dev,test]
    extras_require={"dev": ["check-manifest", "pytest"], "test": ["pytest", "pytest-cov"],},
    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #    'sample': ['logging.conf'],
    # },
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages.
    # see http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={"console_scripts": ["sample=sample:main",],},
)
