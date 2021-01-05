"""Settings to override default settings."""

import logging

#
# Override settings
#

HTTP_PORT = 8888
HTTP_ADDRESS = '127.0.0.1'

#
# Set logging level
#
logging.getLogger().setLevel(logging.DEBUG)

JOB_CLASS_PACKAGES = ['simple_scheduler.jobs']
