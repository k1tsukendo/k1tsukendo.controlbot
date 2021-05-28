# -*- coding: utf-8 -*-
from hentai import Hentai, Format
from functionality import confirm

def getby_id(cmd):
	id = int(cmd.replace('nhentai', '').strip())
	if len(str(id)) > 6:
		print(f'{id} is not a manga id! So... Zero Two.')
		id = 281415
	manga = Hentai(id)
	Hentai.exists(manga.id)
	print(f'#{manga.id} :: {manga.title(Format.Pretty)}')
	
	if id != 281415:
		if confirm('proceed download'):
			print('Starting download...\n')
			manga.download(progressbar=True)
			print(f'Downloading {manga.title(Format.Pretty)} Success!\n')
		else:
			print(f'Downloading {manga.title(Format.Pretty)} aborted.\n')
	else:
		manga.download(progressbar=True)
		print('Enjoy.')