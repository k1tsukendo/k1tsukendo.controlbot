# -*- coding: utf-8 -*-
import requests
import os
import functionality as fc
from logger import *


def get_image():
	URL = input(': >_< : Requires URL : >>> ')
	try:		
		r = requests.get(URL)	
		filename = input(': >_< : Requires Filename : >>> ')
		dir = f'downloaded/{filename}.jpg'
		if os.path.exists(dir):
			if fc.confirm('rewrite file'):
				with open(dir, 'wb') as fd:
					for chunk in r.iter_content(12):
						fd.write(chunk)
			else:
				return
		else:
			with open(dir, 'wb') as fd:
				for chunk in r.iter_content(12):
					fd.write(chunk)
				print(f'Success! File saved as {dir}')
	except:
		logger.critical('THIS IS NOT A URL!')