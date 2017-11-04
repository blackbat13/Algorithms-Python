def wyszukiwanie_binarne_iteracyjnie(tablica, liczba):
    lewy = 0
    prawy = len(tablica) - 1
    while lewy < prawy:
        środek = int((lewy + prawy) / 2)
        if liczba < tablica[środek]:
            prawy = środek
        elif liczba > tablica[środek]:
            lewy = środek + 1
        else:
            return środek

    if lewy < len(tablica) and tablica[lewy] == liczba:
        return lewy

    return -1


def wyszukiwanie_binarne_rekurencyjnie(tablica, liczba, lewy, prawy):
    if lewy < prawy:
        środek = int((lewy + prawy) / 2)
        if liczba < tablica[środek]:
            return wyszukiwanie_binarne_rekurencyjnie(tablica, liczba, lewy, środek)
        elif liczba > tablica[środek]:
            return wyszukiwanie_binarne_rekurencyjnie(tablica, liczba, środek + 1, prawy)
        else:
            return środek
    elif lewy < len(tablica) and tablica[lewy] == liczba:
        return lewy

    return -1


tablica = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liczba = int(input('Podaj liczbę do znalezienia: '))
indeks1 = wyszukiwanie_binarne_iteracyjnie(tablica, liczba)
indeks2 = wyszukiwanie_binarne_rekurencyjnie(tablica, liczba, 0, len(tablica))
if indeks1 != indeks2:
    print('Sprzeczne wyniki')
elif indeks1 != -1:
    print(f'Indkes szukanego elementu to {indeks1}')
else:
    print('Nie znaleziono szukanej wartości')
