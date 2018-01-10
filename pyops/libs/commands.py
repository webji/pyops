#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 15:24:10

import os

class commands:
    def __init__(self, command):
        self.command=command

    def execute(self):
        result = os.popen(self.command)
        results = result.readlines()
        return results