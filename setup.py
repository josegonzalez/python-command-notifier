#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2014 Jose Diaz-Gonzalez

# This file is part of command-notifier.

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from command_notifier import __version__
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))


setup(
    name='command-notifier',
    version=__version__,
    author='Jose Diaz-Gonzalez',
    author_email='email@josediazgonzalez.com',
    packages=['command_notifier'],
    scripts=['bin/cn-publish', 'bin/cn-subscribe'],
    url='https://github.com/josegonzalez/python-command-notifier',
    license=open('LICENSE.txt').read(),
    classifiers=[
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    description=''.join([
        'A very simple command-notification package',
        'based on SQS for distributed systems'
    ]),
    long_description=open_file('README.rst').read(),
    install_requires=open_file('requirements.txt').readlines(),
    zip_safe=True,
)
