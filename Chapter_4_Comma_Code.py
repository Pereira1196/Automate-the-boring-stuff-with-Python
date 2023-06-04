#Programa para testar o uso de listas
while True:
    try:
        print('Insira uma lista:')
        entrada = list(input())
        lista = []
        auxiliar = ''
        if ('[' or '(' or ')' or ']' or ',') in entrada:
            while ('[' or '(' or ')' or ']' or ',') in entrada:
                if '[' in entrada:
                    entrada.remove ('[')
                if '(' in entrada:
                    entrada.remove ('(')
                if ']' in entrada:
                    entrada.remove (']')
                if ')' in entrada:
                    entrada.remove (')')
                if ',' in entrada:
                    quebra = entrada.index(',')
                    for index, item in enumerate(entrada):
                        if index == (quebra):
                            del entrada[0:quebra]
                            entrada.remove(',')
                        else:
                            auxiliar += item
                    lista.append(auxiliar)
                    auxiliar = ''
        for index, item in enumerate(entrada):
            auxiliar += item
        lista.append(auxiliar)
        auxiliar = ''
        texto=''
        if lista == ['']:
            print('Valor inválido. Tente novamente.', end=' ')
            continue
        for index, item in enumerate(lista):
            if index == (len(lista)-1):
                texto += 'and '
                texto += item
            else:
                texto += item + ', '
        print(texto)
        break
    except:
        print('Valor inválido, tente novamente')
        continue