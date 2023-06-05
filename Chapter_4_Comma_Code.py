"""
Programa para testar o uso de listas
Autor: Douglas Silva
Data: 04/06/2023
"""

while True:
    try:

 #Declaração das variáveis
        print('Insira uma lista:')
        entrada = list(input())
        lista = [] #Auxiliar para criar a lista a ser transformada em texto
        auxiliar = '' #Auxiliar para pegar os elementos da lista inserida
        checar = ['[', '(', ')', ']', ',', ' ', '{', '}'] #Auxiliar com os símbolos para entender que é lista ou tupla
        texto = '' #texto a ser exibido no final
        listaAuxiliar = list() #Auxiliar para saber onde estão os espaços e as vírgulas
        proxCaracEspecial = 0 #Auxiliar para determinar o próximo espaço ou vírgula
        contador = 0 #Auxiliar para ajudar no cálculo do próximo espaço ou vírgula

#Condicionais para ver se o que foi inserido é uma lista ou tupla ou palavras individuais
        if any(value in checar for value in entrada):
            for indice, value in enumerate(entrada):
                if value == ',':
                    listaAuxiliar.append(indice)
                elif value == ' ':
                    listaAuxiliar.append(indice)
                elif '[' in entrada:
                    entrada.remove ('[')
                elif '(' in entrada:
                    entrada.remove ('(')
                elif '{' in entrada:
                    entrada.remove ('{')
            while any(value in checar for value in entrada):
                if (',' in entrada) or (' ' in entrada):
                    quebra = listaAuxiliar[0]
                    for index, item in enumerate(entrada):
                        if index == (quebra):
                            del entrada[0:quebra]
                            del entrada[0]
                            proxCaracEspecial = proxCaracEspecial + listaAuxiliar[0]
                            contador += 1
                            if len(listaAuxiliar) > 1:
                                listaAuxiliar[1] = listaAuxiliar[1] - proxCaracEspecial - contador
                            del listaAuxiliar[0]
                            break
                        else:
                            auxiliar += item
                    if auxiliar != '':
                        lista.append(auxiliar)
                        auxiliar = ''
                elif ']' in entrada:
                    entrada.remove (']')
                elif ')' in entrada:
                    entrada.remove (')')
                elif '}' in entrada:
                    entrada.remove ('}')
        for index, item in enumerate(entrada):
            auxiliar += item
        if auxiliar != '':
            lista.append(auxiliar)

        #Checa se a lista está vazia
        if lista == []:
            print('Valor inválido. Tente novamente.', end=' ')
            continue

        #Adiciona cada elemento da lista na string e a exibe
        print(lista)
        for index, item in enumerate(lista):
            if index == (len(lista)-1):
                texto += 'and '
                texto += item
            else:
                texto += item + ', '
        print(texto)
        break
    
    #Caso haja algum erro pede para o usuário inserir uma nova lista
    except:
        print('Valor inválido, tente novamente')
        continue