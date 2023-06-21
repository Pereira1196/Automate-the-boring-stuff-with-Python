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

for indiceLinha, linha in enumerate(grid):
    for indiceImagem, imagem in enumerate(linha):
        if indiceImagem == len(linha)-1:
            print(imagem)
        else:
            print(imagem, end='')