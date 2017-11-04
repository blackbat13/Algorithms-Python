def sortowanie_przez_zliczanie(tablica):
    wystąpienia = []
    for i in range(0, 101):
        wystąpienia.append(0)

    for liczba in tablica:
        wystąpienia[liczba] += 1

    wynik = []
    for i in range(0, len(wystąpienia)):
        for j in range(0, wystąpienia[i]):
            wynik.append(i)

    return wynik


tablica = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
posortowana_tablica = sortowanie_przez_zliczanie(tablica)
print(posortowana_tablica)
