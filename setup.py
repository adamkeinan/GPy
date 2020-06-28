#!/usr/bin/env python
# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.
from __future__ import (
    absolute_import,
    division,
    print_function,
)

import os
import re
import django

from setuptools import setup


base_dir = os.path.dirname(__file__)

about = {}
with open(os.path.join(base_dir, "pipfile", "__about__.py")) as f:
    exec(f.read(), about)

with open(os.path.join(base_dir, "README.rst")) as f:
    long_description = f.read()

with open(os.path.join(base_dir, "CHANGELOG.rst")) as f:
    # Remove :issue:`ddd` tags that breaks the description rendering
    changelog = re.sub(
        r":issue:`(\d+)`",
        r"`#\1 <https://github.com/pypa/pipfile/issues/\1>`__",
        f.read(),
    )
    long_description = "\n".join([long_description, changelog])

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__summary__"],
    long_description=long_description,
    license=about["__license__"],
    url=about["__uri__"],
    author=about["__author__"],
    author_email=about["__email__"],
    install_requires=["toml", "django", "selenium"],
    classifiers={
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Dart",
        "Programming Language :: Dart :: 6.8",
        "Programming Language :: Django",
        "Programming Language :: Django :: 2.1",
        "Programming Language :: Django :: 2.2",
        "Programming Language :: Django :: 2.3",
        "Programming Language :: Django :: 2.4",
        "Programming Language :: Django :: 2.5",
        "Programming Language :: Django :: 2.6",
        "Programming Language :: Django :: 2.7",
        "Programming Language :: Django :: 2.8",
        "Programming Language :: Django :: 2.9",
        "Programming Language :: Django :: 3.0",
        "Programming Language :: Django :: 2.2",
        "Programming Language :: Vue.js",
        "Programming Language :: Vue.js :: 2.5",
        "Programming Language :: Vue.js :: 2.6",
    },
    packages=["pipfile",],
)
