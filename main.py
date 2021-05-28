# -*- coding: utf-8 -*-
from logger        import *
logger.info('main.py: including libs...')
logger.info('main.py: preparing to run...')

from functionality import *
from commands_list import *
from downloader    import *
from nhentai       import *
from time          import time
from threading     import Thread
logger.info('main.py: main: done.\n')


def main():
	running = True
	while running:
		command = input(': >_< : ')
		if COMMANDS[0] in command:   print(echo(command))  # echo
		elif command == COMMANDS[1]: print(now_time())  # time
		elif command == COMMANDS[2]: print(device())  # device
		elif command == COMMANDS[3]: clear_term()
		elif command == COMMANDS[4]: exit_console(running)
		elif command == COMMANDS[5]: get_image()
		elif COMMANDS[6] in command: getby_id(command)

		else:
			try:
				eval(command)
			except:
				logger.error(f'k1tsukendo: command {command} not found.')

if __name__ == '__main__': sys.exit(main())
