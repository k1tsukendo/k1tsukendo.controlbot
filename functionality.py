# -*- coding: utf-8 -*-

import sys
from time import sleep
from platform import *
from datetime import *
from os import system as syst


def confirm(what=None, default='y'):
    if what is None:
        prompt = input(f'Are you sure? [Y/n] ({default})')
    else:
        prompt = input(f'Are you sure want to {what}? [Y/n] ({default}) ')
    if prompt.lower() == 'y':
        return True
    elif prompt.lower() == 'n':
        return None
    elif prompt == '':
        if default == 'y':
            return True
        elif default == 'n':
            return None

# time
def now_time():
    now = datetime.now()
    return f'Your local time is {now.hour}:{now.minute}.'

# echo
def echo(command): 
    return command.replace('echo', '').strip()

# device info
def device(): 
    return f'Arch:    {architecture()[0]}\nSystem:  {system()}\nHost:    {node()}'

# Terminal
def clear_term(): 
    syst('cls || clear')

def exit_console(confirmation=True):
    if confirmation:
        if confirm('quit'):
            sys.exit()
        else: 
            return
    else:
        sys.exit()
