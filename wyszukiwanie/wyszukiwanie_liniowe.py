def wyszukiwanie_liniowe(tablica, liczba):
    for i in range(0, len(tablica)):
        if liczba == tablica[i]:
            return i

    return -1


tablica = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liczba = int(input('Podaj liczbę do znalezienia: '))
index = wyszukiwanie_liniowe(tablica, liczba)
if index == -1:
    print('Nie znaleziono podanej wartości')
else:
    print(f'Szukana liczba znajduje się na pozycji o numerze {index}')
