#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 19:33:12

import os
from collections import defaultdict


command = os.popen('lsb_release -a')
results = command.readlines()

lsb_dict = defaultdict()

for result in results:
    (d_type, d_value) = result.split(':\t')
    lsb_dict[d_type.strip()] = d_value.strip()

# print lsb_dict
for key in lsb_dict:
    print '{} \t -- \t : {}'.format(key, lsb_dict[key])




