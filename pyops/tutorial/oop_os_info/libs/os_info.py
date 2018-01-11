#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 19:59:10

import os
from collections import defaultdict
import datetime

import commands


class OS_CI(object):
    version = 'UNKOWN'
    dist_name = 'UNKOWN'
    dist_release = 'UNKOWN'
    dist_codename = 'UNKOWN'
    kernel = 'UNKOWN'

    def __init__(self):
        super(OS_CI, self).__init__()
        if os.name == 'posix':
            self._get_posix_dist_info()
            self._get_posix_kernel()

        
    def _get_posix_dist_info(self):
        """get the os distribution information
        """

        results = os.popen('lsb_release -a')
        lsb_dict = defaultdict()

        for result in results:
            (d_type, d_value) = result.split(':\t')
            lsb_dict[d_type.strip()] = d_value.strip()

        self.version = lsb_dict.get('Description', 'UNKOWN')
        self.dist_codename = lsb_dict.get('Codename', 'UNKOWN')
        self.dist_name = lsb_dict.get('Distributor ID', 'UNKOWN')
        self.dist_release = lsb_dict.get('Release', 'UNKOWN')


    def _get_posix_kernel(self):
        """get the os kernel information
        """

        command = os.popen('uname -r')
        results = command.readlines()
        if len(results):
            self.kernel = results[0].strip()


    def date(self):
        """get the os date value
        """

        command = os.popen('date')
        results = command.readlines()
        if len(results):
            return results[0].strip()

        





