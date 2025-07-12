stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12 }

def displayInventory(inventory):
    print("invenroy:")
    total_item = 0
    for key, value in inventory.items():
        print(str(value) + ' ' + key)
        total_item += value
    print("Total number of items: " + str(total_item))


#displayInventory(stuff)

def addToInventory(inventory , addItems):
    for item in addItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dragger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragon_loot)
displayInventory(inv)
