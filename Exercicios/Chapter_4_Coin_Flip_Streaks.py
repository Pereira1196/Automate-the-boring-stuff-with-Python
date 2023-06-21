"""
Programa para testar o aprendizado de listas
Autor: Douglas Silva
Data: 04/06/2023
"""

import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    listOfNumbers = []
    for throw in range(100):
        listOfNumbers.append(random.randint(0,1))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    streaks = 0
    for play, throwResult in enumerate(listOfNumbers):
        if streaks == 5:
            numberOfStreaks += 1
            streaks = 0
        elif play == len(listOfNumbers) - 1:
            break
        elif throwResult == listOfNumbers[play + 1]:
            streaks += 1
        else:
            streaks = 0
print('Chance of streak: %s%%' % (numberOfStreaks / 100))