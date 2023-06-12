'''
Projeto para testar conhecimentos de ReGex
Autor: Douglas Silva
Data: 12/06/2023
'''

import re

date = re.compile(r'''(([1-3]\d)
/
([0-1]\d)
/
([1-2]\d{3}))
''', re.VERBOSE)

thirtyDays = ['04', '05', '06', '11']

match = date.findall('29/02/2004')

leapYear = False
if ((int(match[0][3]) % 4 == 0) or (int(match[0][3]) % 100 == 0) or (int(match[0][3]) % 400 == 0)):
    leapYear = True

for groups in match:
    if int(groups[1]) > 31:
        print('Data inválida')
    elif int(groups[2]) > 12:
        print('Data inválida')
    elif groups[2] in thirtyDays and int(groups[1]) > 30:
        print('Data inválida')
    elif (groups[2] == '02' and int(groups[1]) > 28 and leapYear == False):
        print('Data inválida')
    elif (groups[2] == '02' and int(groups[1]) > 29 and leapYear == True):
        print('Data inválida')
    else:
        print('Data válida')