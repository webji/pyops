#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 13:25:12


import logging

try:
    import curses
except ImportError:
    curses = None

# class SaveLogHandler(logging.Handler):
#     """LogHandler that save records to a list
#     """

#     def __init__(self, saveto=None, *args, **kwargs):
#         self.saveto = saveto
#         logging.Handler.__init__(self, *args, **kwargs)

#     def emit(self, record):
#         if self.saveto is not None:
#             self.saveto.append(record)

#     handle = emit


# def enable_pretty_logging(logger=logging.getLogger()):
#     channel = logging.StreamHandler()
#     channel.setFormatter(LogFormatter())
#     logger.addHandler(channel)

