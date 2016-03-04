#!/usr/bin/env python
# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

from __future__ import unicode_literals
import argparse
import os
import sys

from unittest import TextTestRunner

'''
The try statement is used to add python 2.6 support.
The unittest in python 2.6 doesn't have the loader function so
if the ImportError is thrown, it will switch and import unittest2
which is a module that has backported the 2.7 unittest to older
versions of python.
'''
try:
    from unittest import loader
except ImportError:
    from unittest2 import loader

parser = argparse.ArgumentParser("Run unit tests.")
parser.add_argument('-n', '--name', help='the name of the test to run',
                    metavar='NAME')

args = parser.parse_args()

test_path = os.path.join(os.path.dirname(__file__), 'tests')
test_loader = loader.TestLoader()
if args.name:
    test_loader.testMethodPrefix = args.name

result = TextTestRunner(verbosity=2).run(test_loader.discover(test_path))
sys.exit(len(result.errors) + len(result.failures))
