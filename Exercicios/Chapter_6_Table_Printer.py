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
for i in range(len(tableData)):
    for palavra in tableData[i]:
        if len(palavra) > maiorPalavra[i]:
            maiorPalavra[i] = len(palavra)

#Adiciona cada palavra na lista
for i in range(len(tableData)):
    for indice, palavra in enumerate(tableData[i]):
        linhaImpressa[indice] = linhaImpressa[indice] + palavra.rjust(maiorPalavra[i]+1)

#Converte a lista em string
linhaImpressa = '\n'.join(linhaImpressa)
print(linhaImpressa)
