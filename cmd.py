# -*- coding: utf-8 -*- 
import sys, time, platform, subprocess
# Package kitsukendo by k1tsukēndø

class BotCmd(object):
	def confirm(self):
		cmd_confirm = input('Are you sure? [Y/N] ')
		if 'y' in cmd_confirm.lower():
			return True
		if 'n' in cmd_confirm.lower():
			return None

	def run(self):
		cmd = input('>_ ')
		if 'echo' in cmd:
			print(cmd.replace('echo', '').strip())
		elif 'time' in cmd:
			import datetime
			now = datetime.datetime.now()
			print(f'here is {now.day}th of {now.month}th, {now.hour}:{now.minute}')

		elif 'math' in cmd:
			print('NOTE::syntax :: Num (+, -, /, //, %, *) Num')
			print(eval(input('>_ .. ')))
		
		elif 'device' in cmd:
			print(f'Net Node  :: {platform.node()}')
			print(f'Processor :: {platform.processor()}')
			print(f'System    :: {platform.system()} {platform.version()}')

		elif '-h' in cmd:
			print('Help for k1tsukendo.controlbot\n')
			print('''
echo   :: returns ur input
time   :: returns ur local time
math   :: returns inputed simple math expression
device :: returns ur device characteristics
anime  :: :)
			''')
		
		elif cmd == 'fuckthatshit':
			print('ok')
			subprocess.Popen("python -c /lol.py")
		elif 'anime' in cmd:
			print('''
SEMPAI! MORE! MORE! I WANT MORE!
PLEASE, MAKE ME INCAPSULATED!!!
USE TIME AND ECHO!! PLEASE!!!!1!1
⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄
 ⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄
⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗
⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄
⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄
⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄
⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿

''')
	
		elif 'ಠ_ಠ' in cmd:
			print('What?')
			time.sleep(1)
			print('What you want?')
			time.sleep(1.5)
			print('Why you bulling me?')
			time.sleep(1)
			print(':\'(')
			time.sleep(.5)
			quit()

		elif 'exit' in cmd:
			if self.confirm():
				sys.exit(print(':Session closed:'))
			else:
				print('Confirmation returned <notabool>.')
				
		else:
			if cmd != '':
				try:
					if cmd != 'quit()':
						eval(cmd)
					else:
						print('R u kidding me??')
				except:
					print(f'k1tsukendo.controlbot :: {cmd} :: command not found.')
