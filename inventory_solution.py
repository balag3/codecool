# GAME INVENTORY ###########################################################
###########################################################################
# under every function uncomment and unindent the function call to test it


# inventory
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


# display_inventory function

def display_inventory(dic):
    total = sum(inv.values())
    print("Inventory:")
    for i in dic:
        print(i, dic[i])
    print("Total number of items : %s" % (total))

# uncomment it to run the function:
# display_inventory(inv)

# dragon_loot
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


# add_to_inventory function

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

# uncomment it to run the function:
# add_to_inventory(inv, dragon_loot)


# print_table function

def print_table(order=None):
    total = sum(inv.values())
    max_length = max([len(i) for i in inv.keys()]) + 9
    max_value_length = max([len(str(i)) for i in inv.values()]) + 3
    if order is None:
        keywords = list(inv)
    elif order == "count,asc":
        keywords = sorted(inv, key=inv.get)
    elif order == "count,desc":
        keywords = sorted(inv, key=inv.get)[::-1]
    print(
           "Inventory:\n{count:>{max3}}{item:>{max}}\n{padding:->{max2}} "
           .format(
                   padding="", count="count", item="item", max=max_length + 1,
                   max2=max_length + max_value_length + 1,
                   max3=max_value_length
                   )
        )
    for i in keywords:
        print('{0:>{max3}} {1:>{max}}'.format(
            inv[i], i, max=max_length, max3=max_value_length))
    print('{padding:->{max2}}'.format(padding="",
                                      max2=max_length + max_value_length + 1))
    print("Total number of items : %s" % (total))


# uncomment it to run the function:
# print_table()
# print_table("count,asc")
# print_table("count,desc")


# import_inventory function

def import_inventory(filename):
    with open(filename, "r")as myfile:
        a = myfile.readlines()
        b = [line.rstrip('\n')for line in a][1:]
        c = dict([item.split(',') for item in b])
        for i in c:
            if i not in inv:
                inv.update({i: c[i]})
            else:
                inv[i] += int(c[i])
        return inv

# uncomment it to run the function:
# import_inventory("your_preferred_file.txt")


# export_inventory function

def export_inventory(filename="export_inventory.csv"):
    items = list(inv.items())
    with open(filename, "w")as myfile:
        for i in items:
            myfile.write("{0},{1}\n".format(i[0], i[1]))

# uncomment it to run the function:
# export_inventory()
