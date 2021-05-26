# -*- coding: utf-8 -*-
from logger        import *
logger.info('main.py: including libs...')
logger.info('main.py: preparing to run...')

from functionality import *
from commands_list import *
logger.info('main.py: main: done.\n')


def main():
	
	while 1:
		command = input(': >_ : ')
		if COMMANDS[0] in command:   print(echo(command))  # echo
		elif command == COMMANDS[1]: print(now_time())  # time
		elif command == COMMANDS[2]: print(device())  # device
		elif command == COMMANDS[3]: clear_term()

if __name__ == '__main__': sys.exit(main())
