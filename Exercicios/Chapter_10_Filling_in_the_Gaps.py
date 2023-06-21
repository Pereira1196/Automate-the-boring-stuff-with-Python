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
for endereco in enderecoArquivos:
    nomeArquivo = os.path.basename(endereco)
    arquivos.append(nomeArquivo)

for numArquivo, arquivo in enumerate(arquivos):
    if ((numArquivo < 9) and arquivo != ('spam00' + str(numArquivo+1) + '.txt')):
        newName = 'spam00' + str(numArquivo+1) + '.txt'
        shutil.move(enderecoArquivos[numArquivo], Path(os.path.dirname(enderecoArquivos[numArquivo])) / newName)
    elif ((numArquivo < 99) and arquivo != ('spam0' + str(numArquivo+1) + '.txt')):
        newName = 'spam0' + str(numArquivo+1) + '.txt'
        shutil.move(enderecoArquivos[numArquivo], Path(os.path.dirname(enderecoArquivos[numArquivo])) / newName)
    else:
        newName = 'spam' + str(numArquivo+1) + '.txt'
        shutil.move(enderecoArquivos[numArquivo], Path(os.path.dirname(enderecoArquivos[numArquivo])) / newName)
