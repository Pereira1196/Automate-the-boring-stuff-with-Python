#Este programa foi feito para testar o aprendizado de funções, condicionais, laços de repetição e try except

def collatz(numero):
    #Função para explorar a sequência collatz
    global number
    if numero % 2 == 0:
        number = numero//2
    else:
        number = 3 * numero + 1
    print(number)
    return number

while True:
    try:
        print('Entre com um número inteiro:')
        number = int(input())
        if number == 0:
           print('Este não é um número válido, tente novamente. ',end='')
           continue 
        break
    except ValueError:
        print('Este não é um número válido, tente novamente. ',end='')
        continue
while number != 1:
    collatz(number)
