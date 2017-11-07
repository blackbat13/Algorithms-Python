import math


def stooge_sort(tablica, początek, koniec):
    if tablica[koniec] < tablica[początek]:
        tmp = tablica[początek]
        tablica[początek] = tablica[koniec]
        tablica[koniec] = tmp

    if koniec - początek + 1 > 2:
        t = math.floor((koniec - początek + 1) / 3)
        stooge_sort(tablica, początek, koniec - t)
        stooge_sort(tablica, początek + t, koniec)
        stooge_sort(tablica, początek, koniec - t)


tablica = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
stooge_sort(tablica, 0, len(tablica) - 1)
print(tablica)
