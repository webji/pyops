#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 15:22:10

import os
import re
from collections import defaultdict
import datetime

from ci import CI
from fs_ci import FS_CI
import commands


class OS_CI(CI):
    version = CI.CI_UNKOWN
    dist_name = CI.CI_UNKOWN
    dist_release = CI.CI_UNKOWN
    dist_codename = CI.CI_UNKOWN
    kernel = CI.CI_UNKOWN
    fs_list = []


    def __init__(self):
        super(OS_CI, self).__init__()
        self.ci = 'OS'
        if os.name == 'posix':
            self._get_posix_dist_info()
            self._get_posix_kernel()

        
    def _get_posix_dist_info(self):
        """get the os distribution information
        """

        L_command = commands.commands('lsb_release -a')
        results = L_command.execute()
        lsb_dict = defaultdict()

        for result in results:
            (d_type, d_value) = result.split(':\t')
            lsb_dict[d_type] = d_value.strip()

        self.version = lsb_dict.get('Description', CI.CI_UNKOWN)
        self.dist_codename = lsb_dict.get('Codename', CI.CI_UNKOWN)
        self.dist_name = lsb_dict.get('Distributor ID', CI.CI_UNKOWN)
        self.dist_release = lsb_dict.get('Release', CI.CI_UNKOWN)


    def _get_posix_kernel(self):
        """get the os kernel information
        """

        L_command = commands.commands('uname -r')
        results = L_command.execute()
        if len(results):
            self.kernel = results[0].strip()


    def _get_posix_fs(self):
        """get the fs information
        """

        if (len(self.fs_list)):
            self.fs_list = []
        L_command = commands.commands('df -h')
        results = L_command.execute()
        results.remove(results[0]) # remove the header
        print results
        for result in results:
            values = result.split()
            print values
            if (len(values) == 6):
                fs_item = FS_CI(values[0], values[1], values[2], values[3], values[4], values[5])
                self.fs_list.append(fs_item)


    def date(self):
        """get the os date value
        """

        L_command = commands.commands('date')
        results = L_command.execute()
        if len(results):
            return results[0].strip()


    def get_fs(self):
        """get the fs information
        """

        if os.name == 'posix':
            self._get_posix_fs()

        
def test():
    os_info = OS_CI()
    print 'OS: {} {} {} {}'.format(os_info.dist_name, os_info.dist_release, os_info.version,os_info.dist_codename) 
    print 'Kernel: {}'.format(os_info.kernel)
    print 'Date: {}'.format(os_info.date())
    os_info.get_fs()
    print os_info.fs_list

if __name__ == '__main__':
    test()





