# -*- coding: utf-8 -*-
from logger   import *
logger.info('functionality.py: including libs..')
logger.info('functionality.py: preparing to run...\n')

from sys      import exit
from time     import sleep
from platform import *
from datetime import *
from os       import system as syst
logger.info('functionality.py: including: done.\n')


def confirm(what=None, default='y'):
	if what is None: prompt = input(f'Are you sure? [Y/n] ({default})')
	else: prompt = input(f'Are you sure want to {what}? [Y/n] ({default}) ')
	if prompt.lower() == 'y':   return True
	elif prompt.lower() == 'n': return None
	elif prompt == '':
		if default == 'y': return True
		elif default == 'n': return None

# time
def now_time():
	now = datetime.now()
	return f'Your local time is {now.hour}:{now.minute}.'

# echo
def echo(command): return command.replace('echo', '').strip()

def device(): return f'Arch: {architecture()[0]};\nSystem: {system()};\nNetName: {node()}'

# Terminal
def clear_term():
	syst('cls || clear')

def exit_console(runbool):
	if confirm('quit'):
		runbool = False
		logger.info('Closing session.')
		logger.info('Shutting down libs...')
		exit(logger.info('Session closed'))

if __name__ != '__main__':
	logger.info('preparing func: <now_time>...')
	logger.info('preparing func: <echo>...')
	logger.info('preparing func: <device>...')
	logger.info('preparing func: <clear_term>...')
	logger.info('preparing func: <exit_console>...')
	logger.info('preparing func: done.\n')