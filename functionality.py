# -*- coding: utf-8 -*-
from logger   import *
logger.info('functionality.py: including libs..')
logger.info('functionality.py: preparing to run...')

from sys      import exit
from time     import sleep
from platform import *
from datetime import *
from requests import get as get_from
from os       import system
logger.info('functionality.py: including: done.')

# time
def now_time():
	now = datetime.now()
	return f'Your local time is {now.hour}:{now.minute}.'
# echo
def echo(command):
	return command.replace('echo', '').strip()
	
def device():
	return 'In dev.'

def clear_term():
	system('cls || clear')