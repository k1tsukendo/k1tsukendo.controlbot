# -*- coding: utf-8 -*-
from logger   import *
logger.info('functionality.py: including libs..')
logger.info('functionality.py: preparing to run...')

from sys      import exit
from time     import sleep
from platform import *
from datetime import *
from requests import get as get_from
from os       import system as syst
logger.info('functionality.py: including: done.')


def confirm(what=None):
	if what is None: prompt = input('Are you sure? [Y/n] ')
	else: prompt = input(f'Are you sure want to {what}? [Y/n] ')
	if prompt.lower() == 'y':   return True
	elif prompt.lower() == 'n': return None

# time
def now_time():
	now = datetime.now()
	return f'Your local time is {now.hour}:{now.minute}.'
# echo
def echo(command):
	return command.replace('echo', '').strip()
	
def device():
	return f'''                    :DEVICE INFO:
Architecture :: {architecture()[0]};
System       :: {system()} {release()};
Net Name     :: {node()};
...          :: {platform()};'''

# Terminal
def clear_term():
	syst('cls || clear')

def exit_console(runbool):
	if confirm('quit'):
		runbool = False
		logger.info('Closing session.')
		logger.info('Shutting down libs...')
		exit(logger.info('Session closed'))
	
