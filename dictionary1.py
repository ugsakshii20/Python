myWallet = {'Diary': 1, 'CCards': 2, 'DCards': 2, 'VCards': 5}

# 1) Add a new credit card
myWallet['CCards'] += 1

# 2) Check if Photograph is available
is_photograph_available = 'Photograph' in myWallet

# 3) Add four Photographs
myWallet['Photographs'] = 4

# 4) Remove Photographs using del() and pop() methods
del myWallet['Photographs']
myWallet.pop('Photographs', None)

# 5) Represent the particulars of the dictionary as a tuple
myWallet_tuple = tuple(myWallet.items())

# 6) Sort items in ascending order based on items
sorted_items = sorted(myWallet.items())

# 7) Sort items in ascending order based on item quantity
sorted_by_quantity = sorted(myWallet.items(), key=lambda item: item[1])

print(f"myWallet after adding a credit card: {myWallet}")
print(f"Is Photograph available: {is_photograph_available}")
print(f"myWallet after adding and removing Photographs: {myWallet}")
print(f"myWallet as a tuple: {myWallet_tuple}")
print(f"Items sorted by name: {sorted_items}")
print(f"Items sorted by quantity: {sorted_by_quantity}")
