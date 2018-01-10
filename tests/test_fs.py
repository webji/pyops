#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 18:41:10

import unittest2 as unittest

from pyops.libs.ci import CI
from pyops.libs.fs_ci import FS_CI

class TestFS(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.fs = FS_CI('rootfs', '448G', '422G', '26G', '95%', '/')

    
    @classmethod
    def tearDownClass(self):
        pass

    def test_dist_info(self):
        self.assertEqual(self.fs.filesystem, 'rootfs')
        self.assertEqual(self.fs.size, '448G')
        self.assertEqual(self.fs.used, '422G')
        self.assertEqual(self.fs.avail, '26G')
        self.assertEqual(self.fs.used_per, '95%')
        self.assertEqual(self.fs.mounted_on, '/')
        