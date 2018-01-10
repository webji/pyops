#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 17:09:10

import os
import re
from collections import defaultdict
import datetime

from ci import CI
import commands


class FS:
    pass


class FS_CI(CI):
    filesystem = CI.CI_UNKOWN
    size = CI.CI_UNKOWN
    used = CI.CI_UNKOWN
    avail = CI.CI_UNKOWN
    used_per = CI.CI_UNKOWN
    mounted_on = CI.CI_UNKOWN

    def __init__(self, filesystem, size, used, avail, used_per, mounted_on):
        super(FS_CI, self).__init__()
        self.ci = 'FS'
        self._get_fs_info(filesystem, size, used, avail, used_per, mounted_on)
    
        
    def _get_fs_info(self, filesystem, size, used, avail, used_per, mounted_on):
        """get the os distribution information
        """
        self.filesystem = filesystem
        self.size = size
        self.used = used
        self.avail = avail
        self.used_per = used_per
        self.mounted_on = mounted_on
        


def test():
    pass

if __name__ == '__main__':
    test()





