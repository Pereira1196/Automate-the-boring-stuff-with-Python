'''
Programa para testar aprendizagem de Dicionários
Autor: Douglas Silva
Data: 04/06/2023
'''
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    '''Mostra os itens que estão no inventario'''
    print("Inventory:")
    itemTotal = 0 #variável para contabilizar o total de itens
    for itemType, quantityItem in inventory.items():
        print(str(quantityItem) + ' ' + itemType)
        itemTotal = itemTotal + quantityItem
    print("Total number of items: " + str(itemTotal))

displayInventory(stuff)