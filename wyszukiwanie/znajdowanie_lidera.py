def znajdź_lidera(tablica):
    licznik = 0
    for el in tablica:
        if licznik == 0:
            obecny_kandydat = el
            licznik = 1
        else:
            if el == obecny_kandydat:
                licznik += 1
            else:
                licznik -= 1

    return obecny_kandydat


def zlicz_wystąpienia(element, tablica):
    licznik = 0
    for el in tablica:
        if el == element:
            licznik += 1

    return licznik


tablica = [1, 2, 5, 5, 7, 5, 5, 10, 5, 5]
lider = znajdź_lidera(tablica)
if zlicz_wystąpienia(lider, tablica) >= len(tablica) / 2:
    print(f'Lider zbioru: {lider}')
else:
    print('W podanej tablicy nie ma lidera')
