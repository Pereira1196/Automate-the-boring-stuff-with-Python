"""
Programa para testar o aprendizado de listas
Autor: Douglas Silva
Data: 04/06/2023
"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for index, item in enumerate(grid):
    for index2, item2 in enumerate(item):
        if index2 == len(item)-1:
            print(item2)
        else:
            print(item2, end='')