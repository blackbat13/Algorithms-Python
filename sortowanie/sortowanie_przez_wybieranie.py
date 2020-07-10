def znajdź_minimum(tablica, początek):
    indeks_minimum = początek
    for i in range(początek + 1, len(tablica)):
        if tablica[i] < tablica[indeks_minimum]:
            indeks_minimum = i

    return indeks_minimum


def sortowanie_przez_wybieranie(tablica):
    for i in range(0, len(tablica)):
        indeks_minimum = znajdź_minimum(tablica, i)
        tmp = tablica[i]
        tablica[i] = tablica[indeks_minimum]
        tablica[indeks_minimum] = tmp


tablica = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
sortowanie_przez_wybieranie(tablica)
print(tablica)
