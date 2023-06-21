'''
Projeto para testar conhecimentos de ReGex
Autor: Douglas Silva
Data: 12/06/2023
'''

import re

dateToEvaluate = re.compile(r'''(([1-3]\d)
/
([0-1]\d)
/
([1-2]\d{3}))
''', re.VERBOSE)

thirtyDaysMonths = ['04', '05', '06', '11']

matchedDates = dateToEvaluate.findall('29/02/2004')

leapYear = False

print(matchedDates[1])
if ((int(matchedDates[0][3]) % 4 == 0) or (int(matchedDates[0][3]) % 100 == 0) or (int(matchedDates[0][3]) % 400 == 0)):
    leapYear = True

for groups in matchedDates:
    if int(groups[1]) > 31:
        print('Data inválida')
    elif int(groups[2]) > 12:
        print('Data inválida')
    elif groups[2] in thirtyDaysMonths and int(groups[1]) > 30:
        print('Data inválida')
    elif (groups[2] == '02' and int(groups[1]) > 28 and leapYear == False):
        print('Data inválida')
    elif (groups[2] == '02' and int(groups[1]) > 29 and leapYear == True):
        print('Data inválida')
    else:
        print('Data válida')