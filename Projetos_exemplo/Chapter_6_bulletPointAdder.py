#! python3
# Chapter_6_bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add stars.
lista = text.split('\r\n')
for index in range(len(lista)):
    lista[index] = '* ' + str(lista[index])
text = '\n'.join(lista)

pyperclip.copy(text)