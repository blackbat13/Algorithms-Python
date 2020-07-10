print('Creating an empty list')
list = []
print(list)

print()

print('Creating list populated with some data')
list = [2, 4, 6, 8]
print(list)

print()

print('Adding single elements to the list')
list.append(10)
list.append(12)
print(list)

print()

print('Creating list containing 10 elements')
print('Yeah... we need to use some kind of loop')
list = []
for i in range(0, 10):
    list.append(i)

print(list)
