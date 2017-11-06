print('Klasyczna pętla for, od 0 do 10 (bez 10)')
for i in range(0, 10):
    print(i)

print()

print('Odwrócona pętla for od 10 do 0 (bez 0)')
for i in range(10, 0, -1):
    print(i)

print()

print('Pętla idąca od 0 do 10 (bez 10) z krokiem równym 2')
for i in range(0, 10, 2):
    print(i)

print()

tablica = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Przechodzenie po elementach tablicy')
for el in tablica:
    print(el)

print()

print('Przechodzenie po elementach tablicy używając indeksów')
for i in range(0, len(tablica)):
    print(tablica[i])

print()

i = 0
print('Klasyczna pętla while')
while i < 10:
    print(i)
    i += 1

print()
