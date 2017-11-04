import math


def sortowanie_szybkie(tablica, lewy, prawy):
    if prawy <= lewy:
        return

    pivot = tablica[math.floor((lewy + prawy) / 2)]
    i = lewy
    j = prawy
    while i <= j:
        while tablica[i] < pivot:
            i += 1

        while tablica[j] > pivot:
            j -= 1

        if i > j:
            break

        tmp = tablica[i]
        tablica[i] = tablica[j]
        tablica[j] = tmp

        i += 1
        j -= 1

    sortowanie_szybkie(tablica, lewy, j)
    sortowanie_szybkie(tablica, i, prawy)


tablica = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
sortowanie_szybkie(tablica, 0, len(tablica) - 1)
print(tablica)
