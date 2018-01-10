#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 12:04:12


import os
import unittest2 as unittest

all_suite = unittest.TestLoader().discover(os.path.dirname(__file__), "test_*.py")
