# -*- coding: utf-8 -*- 
import sys
# Package kitsukendo by k1tsukēndø

class BotCmd(object):
	def quitconfirm(self):
		cmd_exitconfirm = input('Are you sure want to exit? [Y/N] ')
		if 'y' in cmd_exitconfirm.lower():
			return True
		if 'n' in cmd_exitconfirm.lower():
			return None

	def run(self):
		cmd = input('>_ ')
		if 'echo' in cmd:
			print(cmd.replace('echo', '').strip())
		elif 'time' in cmd:
			import datetime
			now = datetime.datetime.now()
			print(f'here is {now.day}th of {now.month}th, {now.hour}:{now.minute}')
		elif 'exit' in cmd:
			if self.quitconfirm():
				sys.exit(print(':Session closed:'))
			else:
				print('Confirmation returned <notabool>.')
