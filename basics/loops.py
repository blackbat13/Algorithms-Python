print('Classic for loop, from 0 to 10 non inclusive')
for i in range(0, 10):
    print(i)

print()

print('Reverse loop going from 10 to 0 non inclusive')
for i in range(10, 0, -1):
    print(i)

print()

print('Loop going from 0 to 10 non inclusive with loop step := 2')
for i in range(0, 10, 2):
    print(i)

print()

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Looping over elements in a list')
for el in list:
    print(el)

print()

print('Looping over elements in a list using index')
for i in range(0, len(list)):
    print(list[i])

print()

i = 0
print('Classic while loop')
while i < 10:
    print(i)
    i += 1

print()
