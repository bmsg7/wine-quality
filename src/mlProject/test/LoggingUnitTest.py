import logging

# basic
name = 'John'
logging.error('%s raised an error', name)

# test  severiaty 
'''
DEBUG
INFO
WARNING
ERROR
CRITICAL
'''
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info=True)
