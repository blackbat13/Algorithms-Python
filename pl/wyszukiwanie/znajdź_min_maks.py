import math


def znajdź_min_maks_naiwnie(tablica):
    min = tablica[0]
    maks = tablica[0]
    for i in range(1, len(tablica)):
        if tablica[i] < min:
            min = tablica[i]
        if tablica[i] > maks:
            maks = tablica[i]

    return [min, maks]


def znajdź_min_maks_optymalnie(tablica):
    kandydaci_minimum = []
    kandydaci_maksimum = []
    for i in range(1, len(tablica), 2):
        if tablica[i - 1] < tablica[i]:
            kandydaci_minimum.append(tablica[i - 1])
            kandydaci_maksimum.append(tablica[i])
        else:
            kandydaci_minimum.append(tablica[i])
            kandydaci_maksimum.append(tablica[i - 1])

    if len(tablica) % 2 != 0:
        kandydaci_minimum.append(tablica[len(tablica) - 1])
        kandydaci_maksimum.append(tablica[len(tablica) - 1])

    min = kandydaci_minimum[0]
    maks = kandydaci_maksimum[0]
    for i in range(1, len(kandydaci_minimum)):
        if min > kandydaci_minimum[i]:
            min = kandydaci_minimum[i]
        if maks < kandydaci_maksimum[i]:
            maks = kandydaci_maksimum[i]

    return [min, maks]


def znajdź_min_maks_rekurencyjnie(tablica, lewy, prawy):
    if lewy == prawy:
        return [tablica[lewy], tablica[lewy]]

    środek = math.floor((lewy + prawy) / 2)
    lewy_min_maks = znajdź_min_maks_rekurencyjnie(tablica, lewy, środek)
    prawy_min_maks = znajdź_min_maks_rekurencyjnie(tablica, środek + 1, prawy)
    min_maks = [0, 0]
    if lewy_min_maks[0] < prawy_min_maks[0]:
        min_maks[0] = lewy_min_maks[0]
    else:
        min_maks[0] = prawy_min_maks[0]

    if lewy_min_maks[1] > prawy_min_maks[1]:
        min_maks[1] = lewy_min_maks[1]
    else:
        min_maks[1] = prawy_min_maks[1]

    return min_maks


tablica = [3, 6, 1, 9, 10, 4, -4, 6, 12, 5, 11]
print('Algorytm naiwny: ')
wynik = znajdź_min_maks_naiwnie(tablica)
print(f'Minimum: {wynik[0]}, Maksimum: {wynik[1]}')

print('Algorytm optymalny: ')
wynik = znajdź_min_maks_optymalnie(tablica)
print(f'Minimum: {wynik[0]}, Maksimum: {wynik[1]}')

print('Algorytm rekurencyjny: ')
wynik = znajdź_min_maks_rekurencyjnie(tablica, 0, len(tablica) - 1)
print(f'Minimum: {wynik[0]}, Maksimum: {wynik[1]}')
