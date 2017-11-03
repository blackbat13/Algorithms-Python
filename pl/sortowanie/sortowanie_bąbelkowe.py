def sortowanie_bąbelkowe(tablica):
    for i in range(0, len(tablica) - 2):
        for j in range(len(tablica) - 1, i, -1):
            if tablica[j - 1] > tablica[j]:
                tmp = tablica[j]
                tablica[j] = tablica[j - 1]
                tablica[j - 1] = tmp


tablica = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
sortowanie_bąbelkowe(tablica)
print(tablica)
