#!/usr/bin/env python

"""
Global Python log configuration settings
@author mblum
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

import logging
import os
import sys, traceback

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

LOG_FORMAT = '[%(asctime)s] [%(levelname)s] [%(name)s] : %(message)s'
LOG_DATE_FORMAT = '%Y %b %d %a %H:%M:%S'
OFFSET = '\t'*5

class Log4Py(logging.Logger):
    def _log(self, level, msg, args, exc_info=None, extra=None):
        # call parent logging method
        super(Log4Py, self)._log(level, msg, args, exc_info, extra)
        metadata = None
        if len(args) == 0:
            pass
        elif (args is not None) and (args[0] is not None):
           metadata = args[0]
           if 'exception' in metadata:
                exception = metadata['exception']
                exc_type, exc_value, exc_traceback = sys.exc_info()
                stack_trace_header = traceback.format_exception_only(type(exception), exception)
                # remove newlines
                for index, line in enumerate(stack_trace_header):
                    stack_trace_header[index] = line.replace('\n', '')
                stack_trace_body = traceback.format_exc().splitlines()
                stack_trace = stack_trace_header + stack_trace_body
                super(Log4Py, self)._log(level, '\n{}'.format(OFFSET).join(stack_trace), args)

def getLogger(name, filename=None, level='debug'):
    """
    Instantiate a global logger
    LOG_FILE - defaults to temp.log in the working directory
    LOG_LEVEL - defaults to DEBUG
    Find configuration details here:
    https://docs.python.org/2/howto/logging-cookbook.html
    """
    log_file = filename
    log_level = level
    logging.basicConfig(level=LEVELS[log_level],
                        format=LOG_FORMAT,
                        datefmt=LOG_DATE_FORMAT,
                        filename=log_file)
    # setup custom logger
    logging.setLoggerClass(Log4Py)
    logger = logging.getLogger(name)
    return logger