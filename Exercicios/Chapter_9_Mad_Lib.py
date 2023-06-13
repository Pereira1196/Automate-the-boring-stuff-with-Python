''''
Programa para avaliar mexer em arquivos
Autor: Douglas Silva
Data: 13/06/2023

Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE,
NOUN, ADVERB, or VERB appears in the text file.
'''

from pathlib import Path
import re

endereco = Path.cwd()
nomeArquivo = 'madlib.txt'
enderecoArquivo = endereco / nomeArquivo

novasPalavras = list()
texto = enderecoArquivo.read_text()
arquivo = open(enderecoArquivo, 'a')
palavras = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
palavrasEncontradas = palavras.findall(texto)
if palavrasEncontradas != []:
    for palavra in palavrasEncontradas:
        print(f'Digite um {palavra}:')
        texto = re.compile(palavra).sub(input(), texto, count=1)
        print(texto)
arquivo.write('\n\n' + texto)
arquivo.close()
