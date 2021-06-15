# -*- coding: utf-8 -*-
import time as timer
print('Starting k1tsukendo.controlbot...')

HAS_PYFIGLET = True
HAS_COLORAMA = True


print('Loading... 10% |')
from functionality import *
from commands_list import *
from downloader import *
from nhentai import *

from threading import Thread

print ("\033[A                       \033[A")
print("Loading... 30% /")
# This is main dependencies
# Checks only them
try: import pyfiglet
except ImportError as e:
    if 'pyfiglet' in str(e):
        HAS_PYFIGLET = False

print ("\033[A                       \033[A")
print("Loading... 70% —")

try: import colorama
except ImportError as e:
    if 'colorama' in str(e):
        HAS_COLORAMA = False
if HAS_COLORAMA:
    colorama.init()

print ("\033[A                       \033[A")
print("Loading... 100% \\")
print ("\033[A                       \033[A")
print("Running...")

timer.sleep(.8)

print ("\033[A                       \033[A")
print ("\033[A                       \033[A")

def main():

    while True:
        if HAS_COLORAMA:
            command = input(colorama.Fore.GREEN + ': >_< : ' + colorama.Style.RESET_ALL)
        else:
            command = input(': >_< : ')
        if COMMANDS[0] in command:   print(echo(command))  # echo
        elif command == COMMANDS[1]: print(now_time())  # time
        elif command == COMMANDS[2]: print(device())  # device
        elif command == COMMANDS[3]: clear_term()
        elif command == COMMANDS[4]: exit_console()
        elif command == COMMANDS[5]: get_image()
        elif COMMANDS[6] in command:
            if 'search' in command:
                searchby_id(command)
            if 'get' in command:
                getby_id(command)
        else:
            try:
                eval(command)
            except:
                if HAS_COLORAMA:
                    print(colorama.Fore.RED + f'[k1tsųkēndø] : command \'{command}\' not found.' + colorama.Style.RESET_ALL)

                else:
                    print(f'[k1tsųkēndø] : command \'{command}\'')

if __name__ == '__main__':
    if HAS_COLORAMA and HAS_PYFIGLET:

        print(colorama.Fore.MAGENTA + pyfiglet.figlet_format("k1tsukendo", font='slant') + colorama.Style.RESET_ALL)
        print(colorama.Fore.YELLOW + device() + colorama.Style.RESET_ALL + '\n')

    else:
        print('Requirements not found. Running in lite mode.\n')
        print(device() + '\n')
        print('System control bot by k1tsųkēndø')

    Thread(target=sys.exit(main())).run()
