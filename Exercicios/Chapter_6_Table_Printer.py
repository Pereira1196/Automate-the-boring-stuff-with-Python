'''
Exercício para consolidar a manipulação de strings
Autor: Douglas Silva
Data: 08/06/2023
'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
maiorPalavra = [0] * len(tableData) #Variável auxiliar para calcular a maior palavra de cada lista
linhaImpressa = [''] * len(tableData[0]) #Variável auxiliar que irá imprimir o texto na tela

#Calcula a maior palavra
for lista in range(len(tableData)):
    for palavra in tableData[lista]:
        if len(palavra) > maiorPalavra[lista]:
            maiorPalavra[lista] = len(palavra)

#Adiciona cada palavra na lista
for lista in range(len(tableData)):
    for indice, palavra in enumerate(tableData[lista]):
        linhaImpressa[indice] = linhaImpressa[indice] + palavra.rjust(maiorPalavra[lista]+1)

#Converte a lista em string
linhaImpressa = '\n'.join(linhaImpressa)
print(linhaImpressa)
