'''
Programa para testar conhecimento em Regex
Autor: Douglas Silva
Data: 12/06/2023

Write a function that takes a string and does the same thing as the strip() string method. 
If no other arguments are passed other than the string to strip, then whitespace characters will 
be removed from the beginning and end of the string. Otherwise, the characters specified in the second argument 
to the function will be removed from the string.
'''

import re, sys

leading = re.compile(r'^\s+.+')
trailing = re.compile(r'^.+\s+')
texto = 'a'
avaliar = list(texto)

if (leading.search(texto) != None and trailing.search(texto) != None):
    while avaliar[0] == ' ':
        del avaliar[0]
    while avaliar[-1] == ' ':
        del avaliar[-1]
elif (leading.search(texto) != None and trailing.search(texto) == None):
    while avaliar[0] == ' ':
        del avaliar[0]
elif (leading.search(texto) == None and trailing.search(texto) != None):
    while avaliar[-1] == ' ':
        del avaliar[-1]

print(''.join(avaliar))
