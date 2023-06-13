'''
Projeto para testar validação de input
Autor: Douglas Silva
Data: 13/06/2023

To see how much PyInputPlus is doing for you, try re-creating the multiplication quiz project on your own 
without importing it. This program will prompt the user with 10 multiplication questions, 
ranging from 0 × 0 to 9 × 9. You’ll need to implement the following features:

If the user enters the correct answer, the program displays “Correct!” for 1 second and moves on to the next question.
The user gets three tries to enter the correct answer before the program moves on to the next question.
Eight seconds after first displaying the question, 
the question is marked as incorrect even if the user enters the correct answer after the 8-second limit.

RESOLUÇÃO:
FAZER AS QUESTÕES DE MULTIPLICAÇÃO
AVALIAR A RESPOSTA'''

import pyinputplus as pyip
import random, time

qntyQuestions = 10
correctAnswers = 0

for question in range(qntyQuestions):
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    multiplication = number1 * number2
    try:
        answer = pyip.inputInt('Questão %s: Qual o valor da multiplicação %s x %s ? \n' %(question + 1, number1, number2)\
                               , blockRegexes=[r'.*'], allowRegexes=['^%s$' %(multiplication)], limit=3, timeout=8)
        correctAnswers += 1
        print('Correct!')
        time.sleep(1)
        continue
    except:
        continue
print(f'Você acertou um total de {correctAnswers}')
    