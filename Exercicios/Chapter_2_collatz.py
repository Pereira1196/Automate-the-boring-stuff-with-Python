#Este programa foi feito para testar o aprendizado de funções, condicionais, laços de repetição e try except
#Todas as variáveis de função se iniciarão com z

def collatz(znumber):
    #Função para explorar a sequência collatz
    global number
    if znumber % 2 == 0:
        number = znumber//2
    else:
        number = 3 * znumber + 1
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
