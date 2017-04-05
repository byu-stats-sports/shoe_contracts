#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
import sys
import shoecontracts

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='shoecontracts',
    version=shoecontracts.__version__,
    description="Tools for managing shoe contract data for BYU Sports Statistics.",
    long_description=readme,
    author=shoecontracts.__author__,
    author_email='chrisbeckett7@byu.edu',
    url='https://github.com/byu-stats-sports/shoecontracts',
    packages=find_packages(),
    entry_points = {
        "console_scripts": ['shoecontracts = shoecontracts.__main__:main']
    },
    include_package_data=True,
    install_requires=[
        'nba_py',
        'peewee', 
        'requests-cache',
        'python-dateutil'
    ],
    license=shoecontracts.__licence__,
    zip_safe=False,
    keywords='stats statistics nba shoe contracts',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    #  'https://github.com/stattleship/stattleship-python/tarball/master#egg=stattlepy'
    dependency_links=[
        'http://github.com/seemethere/nba_py/tarball/master#egg=nba_py'
    ]
)
