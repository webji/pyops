#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 16:54:10

import unittest2 as unittest

# import logging
# import logging.config
# logging.config.fileConfig('pyops/logging.conf')

from pyops.libs.ci import CI
from pyops.libs.os_ci import OS_CI

class TestOS(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.os_info = OS_CI()

    
    @classmethod
    def tearDownClass(self):
        pass

    def test_dist_info(self):
        self.assertNotEqual(self.os_info.dist_name, CI.CI_UNKOWN)
        self.assertNotEqual(self.os_info.dist_release, CI.CI_UNKOWN)
        self.assertNotEqual(self.os_info.dist_codename, CI.CI_UNKOWN)
        self.assertNotEqual(self.os_info.version, CI.CI_UNKOWN)
        
    def test_kernel(self):
        self.assertNotEqual(self.os_info.kernel, CI.CI_UNKOWN)

    def test_date(self):
        self.assertNotEqual(self.os_info.date(), CI.CI_UNKOWN)

    def test_fs(self):
        self.os_info.get_fs()
        self.assertNotEqual(len(self.os_info.fs_list), 0)
