# Copyright 2015 Rackspace
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import setup

import sys


install_requires = [
    "github3.py >= 1.0.0a1",
    "cachecontrol[filecache]",
]

if sys.version_info[:2] < (2, 7):
    install_requires += [
        "argparse",
    ]


setup(
    name="gh2",
    version="0.0.0",

    description="Tool to convert GitHub issues to a format",
    long_description=open("README.rst").read(),
    license="Apache 2.0",
    url="https://rackspace.com",

    author="Ian Cordasco",
    author_email="ian.cordasco@rackspace.com",

    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],

    packages=["gh2"],

    entry_points={
        "console_scripts": [
            "gh2csv = gh2.csv:main",
        ],
    },

    install_requires=install_requires,
)
