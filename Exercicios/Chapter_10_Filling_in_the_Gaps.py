'''
Programa para testar manipulação de arquivos
Autor: Douglas Silva
Data: 15/06/2023

Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, 
in a single folder and locates any gaps in the numbering 
(such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.
'''
import shutil, os
from pathlib import Path

caminho = Path.cwd() / 'teste'
enderecoArquivos = list(caminho.glob('spam*.txt'))
arquivos = list()
ultimoNum = 0
for item in enderecoArquivos:
    arquivo = os.path.basename(item)
    arquivos.append(arquivo)

for index, item in enumerate(arquivos):
    if ((index < 9) and item != ('spam00' + str(index+1) + '.txt')):
        newName = 'spam00' + str(index+1) + '.txt'
        shutil.move(enderecoArquivos[index], Path(os.path.dirname(enderecoArquivos[index])) / newName)
    elif ((index < 99) and item != ('spam0' + str(index+1) + '.txt')):
        newName = 'spam0' + str(index+1) + '.txt'
        shutil.move(enderecoArquivos[index], Path(os.path.dirname(enderecoArquivos[index])) / newName)
    else:
        newName = 'spam' + str(index+1) + '.txt'
        shutil.move(enderecoArquivos[index], Path(os.path.dirname(enderecoArquivos[index])) / newName)
