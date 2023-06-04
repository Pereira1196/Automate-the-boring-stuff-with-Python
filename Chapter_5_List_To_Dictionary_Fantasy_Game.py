'''
Programa para testar aprendizagem de Dicionários
Autor: Douglas Silva
Data: 04/06/2023
'''

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0) #valida se já existe. Em caso positivo mantém o valor, em caso negativo cria a chave e coloca o valor com 0
        inventory[item] += 1
    return inventory

def displayInventory(inventory):
    print("Inventory:")
    itemTotal = 0 #variável para contabilizar o total de itens
    for itemType, quantityItem in inventory.items():
        print(str(quantityItem) + ' ' + itemType)
        itemTotal = itemTotal + quantityItem
    print("Total number of items: " + str(itemTotal))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)