import math


def scal(tablica, lewy, prawy, podział):
    długość_scalonej = prawy - lewy
    scalona = []
    indeks1 = lewy
    indeks2 = podział
    for i in range(0, długość_scalonej):
        if indeks1 >= podział:
            scalona.append(tablica[indeks2])
            indeks2 += 1
        elif indeks2 >= prawy:
            scalona.append(tablica[indeks1])
            indeks1 += 1
        elif tablica[indeks1] <= tablica[indeks2]:
            scalona.append(tablica[indeks1])
            indeks1 += 1
        else:
            scalona.append(tablica[indeks2])
            indeks2 += 1

    for i in range(0, długość_scalonej):
        tablica[lewy + i] = scalona[i]


def sortowanie_przez_scalanie(tablica, lewy, prawy):
    if prawy - lewy <= 1:
        return

    podział = math.floor((lewy + prawy) / 2)
    sortowanie_przez_scalanie(tablica, lewy, podział)
    sortowanie_przez_scalanie(tablica, podział, prawy)
    scal(tablica, lewy, prawy, podział)


tablica = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
sortowanie_przez_scalanie(tablica, 0, len(tablica))
print(tablica)
