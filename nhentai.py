# -*- coding: utf-8 -*-
from hentai import Hentai, Format
from functionality import confirm

def getby_id(cmd):
	id = int(cmd.replace('nhentai', '').strip())
	if len(str(id)) > 6:
		print(f'{id} is not a manga id!')
		return
	manga = Hentai(id)
	Hentai.exists(manga.id)
	print(f'{manga.title(Format.Pretty)}. Is it what you want?')
	
	if confirm('proceed download'):
		manga.download(progressbar=True)
		print(f'Downloading {manga.title(Format.Pretty)} Success!')
	else:
		print(f'Downloading {manga.title(Format.Pretty)} aborted.')
