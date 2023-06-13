'''
Programa para testar validação de dados de entrada
Autor: Douglas Silva
Data: 13/06/2023

Write a program that asks users for their sandwich preferences. The program should use PyInputPlus 
to ensure that they enter valid input, such as:

Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
Come up with prices for each of these options, and have your program display a total cost after 
the user enters their selection.
'''

import pyinputplus as pyip

sandwhich = dict()
prices = {'wheat' : 1, 'white' : 1, 'sourdough' : 2,
          'chicken' : 2, 'turkey' : 2, 'ham' :2 , 'tofu': 1.5,
          'cheddar' : 1.5, 'Swiss' : 1.5, 'mozzarella': 1.5,
          'mayo' : 1, 'mustard' : 1, 'lettuce' : 1, 'tomato': 1} 
price = 0
itemPrice = 0
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True, prompt='Choose your bread: \n')
sandwhich.setdefault(bread, 1)
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True, prompt='Choose your protein: \n')
sandwhich.setdefault(protein, 1)
wantCheese = pyip.inputYesNo(prompt='Do you want cheese? \n')
if wantCheese == 'yes':
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True, prompt='Choose your cheese: \n')
    sandwhich.setdefault(cheese, 1)
for complement in ['mayo', 'mustard', 'lettuce', 'tomato']:
    wantComplement = pyip.inputYesNo(prompt='Do you want %s ? \n' %(complement))
    if wantComplement == 'yes':
        sandwhich.setdefault(complement, 1)
qntySandwhiches = pyip.inputInt('How many sandwhiches do you want ? \n')
for key, value in sandwhich.items():
    sandwhich[key] = value * qntySandwhiches
    itemPrice = prices.get(key)*sandwhich.get(key)
    price += itemPrice

print(f'You ordered {qntySandwhiches} of the following sandwhich:')
for key in sandwhich.keys():
    print(key)
print(20*'-')
print(f'The price of your order is {price}')