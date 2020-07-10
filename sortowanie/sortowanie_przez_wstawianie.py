def sortowanie_przez_wstawianie(tablica):
    for i in range(1, len(tablica)):
        j = i
        while j > 0 and tablica[j] < tablica[j - 1]:
            tmp = tablica[j]
            tablica[j] = tablica[j - 1]
            tablica[j - 1] = tmp
            j = j - 1


tablica = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
sortowanie_przez_wstawianie(tablica)
print(tablica)
