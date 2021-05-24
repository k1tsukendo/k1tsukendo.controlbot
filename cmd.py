# -*- coding: utf-8 -*- 
import sys, time, platform, subprocess, os, random
# Package kitsukendo by k1tsukēndø

class BotCmd(object):
	__failed = 0
	__jokes = [
		'unow what does a cow-maniac? wearing leatherman.',
		'cat goes meow, cow goes moo, dog goes woof, hohlinka goes slava ukraine',
		'sometimes i think that vodka is not allowed to hohols to drink.']

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
			inp = input('>_ .. ')
			if inp != 'quit()':
				try:
					print(eval(inp))
				except:
					print("Dafaq?..")
			else:
				print('what s wrong with u? u typed \"math\", so use MATH EXPRESSIONS GODDAMN')
				
		elif 'download' in cmd:
			import requests, threading
			
			def parse(): 
				try:
					print('started download..')
					p = requests.get(cmd.replace("download", '').strip())
					out = open('downloaded.jpg', 'wb')
					out.write(p.content)
					out.close()
					print(f'Download {cmd} success! Way - conbots main catalog.')
				except:
					print('Are u sure that what u wrote is url to image?')

			
			threading.Thread(target=parse())
		
		elif cmd == '--joke':
			print(random.choice(BotCmd.__jokes))
		elif 'device' in cmd:
			print(f'Net Node  :: {platform.node()}')
			print(f'Processor :: {platform.processor()}')
			print(f'System    :: {platform.system()} {platform.version()}')

		elif cmd == '-h':
			print('Help for k1tsukendo.controlbot\n')
			print('''
echo   :: returns ur input
time   :: returns ur local time
math   :: returns inputed simple math expression
device :: returns ur device characteristics
anime  :: :)
--joke :: huh, i think u know what to do

do not try to fucking quit in `eval()` parts of program.
i will kill u. but u can exit in any part of program.

u CANT use 2 commands in one line.    or...?
			''')
		
		elif cmd == 'fuckthatshit':
			print('ok')
			subprocess.Popen("python lol.py")
		elif cmd == 'cls':
			os.system('cls||clear')
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
						print('R u kidding me?')
				except:
					BotCmd.__failed += 1
					if BotCmd.__failed == 5:
						BotCmd.__failed = 0
						print('TYPE FCKN -h U IDIOT')
					if BotCmd.__failed != 5:
						print(f'k1tsukendo.controlbot :: {cmd} :: command not found.')
