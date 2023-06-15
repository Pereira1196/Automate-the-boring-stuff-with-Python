'''
Programa para testar a manipulação de arquivos
Autor: Douglas Silva
Data: 15/06/2023

Write a program that walks through a folder tree and searches for files with a certain file extension 
(such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
'''
import os, re, shutil
from pathlib import Path

extensao = re.compile('.*\.py')
caminho = Path('..')
destino = Path('../..') / 'newDirectory'
for folder, subfolder, file in os.walk(caminho):
    for item in file:
        listaArquivos = extensao.findall(item)
        if listaArquivos != []:
            if not (destino).exists():
                os.mkdir(destino)
            for arquivo in listaArquivos:
                enderecoArquivo = Path(folder) / arquivo
                shutil.copy(str(enderecoArquivo), str(destino))