'''
Projeto para testar conhecimentos de ReGex
Autor: Douglas Silva
Data: 12/06/2023

Write a function that uses regular expressions to make sure the password string it is passed is strong.
A strong password is defined as one that is at least eight characters long, 
contains both uppercase and lowercase characters, and has at least one digit. 
You may need to test the string against multiple regex patterns to validate its strength.
'''

import re

atLeastADigit = re.compile(r'.*\d.*')
atLeastEight = re.compile(r'.{8}.*')
atLeastLower = re.compile(r'.*[a-z].*')
atLeastUpper = re.compile(r'.*[A-Z].*')
strongPassword = False
passWord = 'testaNDO1432143'
if (atLeastADigit.search(passWord) == None or atLeastEight.search(passWord) == None or atLeastLower.search(passWord) == None or atLeastUpper.search(passWord) == None):
    strongPassword = True
    print('A senha não é forte o suficiente')
else:
    print('Senha adequada')