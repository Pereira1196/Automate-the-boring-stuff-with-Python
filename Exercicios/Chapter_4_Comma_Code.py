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
        entradaParaLista = [] #Auxiliar para criar a lista a ser transformada em texto
        pegaCaractere = '' #Auxiliar para pegar os elementos da lista inserida
        identificadorEspecial = ['[', '(', ')', ']', ',', ' ', '{', '}'] #Auxiliar com os símbolos para entender que é lista ou tupla
        texto = '' #texto a ser exibido no final
        posicaoEspacoVirgula = list() #Auxiliar para saber onde estão os espaços e as vírgulas
        proxCaracEspecial = 0 #Auxiliar para determinar o próximo espaço ou vírgula
        contador = 0 #Auxiliar para ajudar no cálculo do próximo espaço ou vírgula

#Condicionais para ver se o que foi inserido é uma lista ou tupla ou palavras individuais
        if any(caractere in identificadorEspecial for caractere in entrada):
            for posicao, caractereIdentificado in enumerate(entrada):
                if caractereIdentificado == ',':
                    posicaoEspacoVirgula.append(posicao)
                elif caractereIdentificado == ' ':
                    posicaoEspacoVirgula.append(posicao)
                elif '[' in entrada:
                    entrada.remove ('[')
                elif '(' in entrada:
                    entrada.remove ('(')
                elif '{' in entrada:
                    entrada.remove ('{')
            while any(caractereSeparador in identificadorEspecial for caractereSeparador in entrada):
                if (',' in entrada) or (' ' in entrada):
                    separaElemento = posicaoEspacoVirgula[0]
                    for posicaoCaractere, caractere in enumerate(entrada):
                        if posicaoCaractere == (separaElemento):
                            del entrada[0:separaElemento+1]
                            proxCaracEspecial = proxCaracEspecial + posicaoEspacoVirgula[0]
                            contador += 1
                            if len(posicaoEspacoVirgula) > 1:
                                posicaoEspacoVirgula[1] = posicaoEspacoVirgula[1] - proxCaracEspecial - contador
                            del posicaoEspacoVirgula[0]
                            break
                        else:
                            pegaCaractere += caractere
                    if pegaCaractere != '':
                        entradaParaLista.append(pegaCaractere)
                        pegaCaractere = ''
                elif ']' in entrada:
                    entrada.remove (']')
                elif ')' in entrada:
                    entrada.remove (')')
                elif '}' in entrada:
                    entrada.remove ('}')
        for posicaoCaractere, caractere in enumerate(entrada):
            pegaCaractere += caractere
        if pegaCaractere != '':
            entradaParaLista.append(pegaCaractere)

    except:
        print('Valor inválido, tente novamente')
        continue

    #Checa se a lista está vazia 
    if entradaParaLista == []:
        print('Valor inválido. Tente novamente.', end=' ')
        continue

        
    assert entradaParaLista != [], 'lista vazia, não deveria cair aqui'

#Adiciona cada elemento da lista na string e a exibe
    for posicaoLista, elemento in enumerate(entradaParaLista):
        if posicaoLista == (len(entradaParaLista)-1):
            texto += 'and '
            texto += elemento
        else:
            texto += elemento + ', '
    print(texto)
    break

#Caso haja algum erro pede para o usuário inserir uma nova lista
