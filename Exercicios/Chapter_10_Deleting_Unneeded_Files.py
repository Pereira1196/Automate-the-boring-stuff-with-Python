'''
Programa para testar manipulação de arquivos
Autor: Douglas Silva
Data: 15/06/2023

It’s not uncommon for a few unneeded but humongous files or folders to take up the bulk of the space on your hard drive.
If you’re trying to free up room on your computer, you’ll get the most bang for your buck by deleting 
the most massive of the unwanted files. But first you have to find them.
Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, 
ones that have a file size of more than 100MB. 
(Remember that to get a file’s size, you can use os.path.getsize() from the os module.) 
Print these files with their absolute path to the screen.
'''
import os
from pathlib import Path

maiores = dict()
home = Path.home()
for folder, subfolder, file in os.walk(home):
    for item in file:
        endereco = Path(folder, item)
        tamanho = os.path.getsize(endereco)
        if tamanho >= 104857600:
            maiores[item] = tamanho
print(maiores)