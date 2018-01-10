#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 19:49:12

import os_info
from os_info import info

print os_info.__version__
print os_info.__name__
print os_info.__file__

values = info.get_os_info()
info.display_os_info(values)

